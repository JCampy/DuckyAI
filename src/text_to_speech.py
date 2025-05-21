import traceback
import torch
from TTS.api import TTS
import os
from pydub import AudioSegment
from pydub.playback import play
import time
import re

class TextToSpeech():

    def __init__(self):
        # hardware to run TTS on
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        #self.text_queue = Queue(maxsize=5)
        # model for our TTS service
        self.tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(self.device)
        #tts_models/en/ljspeech/tacotron2-DDC
        #tts_models/en/ljspeech/fast_pitch
        #self.run_condition = True

    # Method to add text to queue
    #def add_text(self, text):
    #    self.text_queue.put(text)

    # Generating audio and producing TTS 
    def generate_audio(self, text):
        print("Generating audio!")

        clean_text = self.clean_text(text)
        if not text.strip():  # Checks if text is empty or just whitespace
            print("Currently empty...")
            return

        output_path= "src/output/output.wav"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        try:

            print("Attempting to create sound")
            # Creating wav file using TTS
            self.tts.tts_to_file(text=clean_text, file_path=output_path, use_phonemes=False) 

            # Check if file exists immediately after TTS call
            if os.path.exists(output_path):
                print(f"Success: Audio file created at {output_path}")
            else:
                print(f"Failure: Audio file NOT found at {output_path} immediately after generation")


            # Wait a moment for the file to be written
            wait_time = 0
            while not os.path.exists(output_path) and wait_time < 5:
                time.sleep(0.1)
                wait_time += 0.1

            # Check again
            if not os.path.exists(output_path):
                raise FileNotFoundError(f"Audio file was not created: {output_path}")

            print("sound created now pydub")
            audio = AudioSegment.from_wav(output_path)
            play(audio)

            print("Deleting sound file")
            os.remove(output_path)

        except Exception as e:
            print(f"Error processing audio: {e}")
            traceback.print_exc()

    # clean text to avoid errors in convolution step           
    def clean_text(self, text):
        # Remove markdown symbols and unsupported chars
        cleaned = re.sub(r"[\*\#\`\[\]\(\)]", "", text)  # remove *, #, backticks, brackets, parentheses
        # Optionally strip excessive whitespace
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned
    
    # Stopping the audio generation
    #def update_run_condition(self):
    #    self.run_condition = False
    

