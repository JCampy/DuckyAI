import speech_recognition as sr
import faster_whisper
import tempfile
import os
import re


class SpeechToText():

    def __init__(self, model):
        
        self.r = sr.Recognizer() # initializing recognizer
        self.r.dynamic_energy_threshold = True # Adjust dynamically to ambient sound
        self.r.pause_threshold = 1.5

        # whisper model and run method
        model_size = "large-v2" # model for whisper
        print("model started")
        self.model = faster_whisper.WhisperModel(model_size, device="cpu", compute_type="int8")

        print("model running")
        self.run_condition = True
        self.ducky_model = model
        self.rubber_duck_win = None

    def check_speech(self):
        while self.run_condition:
            # capturing audio from microphone
            with sr.Microphone() as source:
                print("Listening for audio...")
                audio = self.r.listen(source) # capturing audio chunk
                print("Processing audio...")
                
                try:

                    # Save audio to a temporary WAV file
                    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                        tmpfile.write(audio.get_wav_data())
                        tmpfile_path = tmpfile.name

                    # transcribing
                    segments, info = self.model.transcribe(tmpfile_path)
                    full_text = " ".join(segment.text for segment in segments)
                    
                    cleaned_text = self.normalize(full_text)
                    activate_trigger = "hey ducky"
                    exit_trigger = "exit"

                    if activate_trigger in cleaned_text:
                        print("hey ducky recognized")
                        os.remove(tmpfile_path)
                        self.capture_audio()
                    elif exit_trigger in cleaned_text:
                        self.rubber_duck_win.handle_exit()
                    else:
                        print("Unknown keyword")

                    os.remove(tmpfile_path)

                except Exception as e:
                    print(f'Error processing audio: {e}')
                    continue

    def capture_audio(self):
        with sr.Microphone() as source:
            print("Listening for audio...")
            audio = self.r.listen(source) # capturing audio chunk
            print("Processing audio...")
            
            try:

                # Save audio to a temporary WAV file
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                    tmpfile.write(audio.get_wav_data())
                    tmpfile_path = tmpfile.name

                # transcribing
                segments, info = self.model.transcribe(tmpfile_path)
                full_text = " ".join(segment.text for segment in segments)
                print(full_text)
                self.ducky_model.ask_ducky(full_text)

            except Exception as e:
                print(f'Error processing audio: {e}')
                    
    '''           
    def capture_audio(self):
        while self.run_condition:
            # capturing audio from microphone
            with sr.Microphone() as source:
                print("Listening for audio...")
                audio = self.r.listen(source) # capturing audio chunk
                print("Processing audio...")
                
                try:

                    # Save audio to a temporary WAV file
                    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                        tmpfile.write(audio.get_wav_data())
                        tmpfile_path = tmpfile.name

                    # transcribing
                    segments, info = self.model.transcribe(tmpfile_path)
                    full_text = " ".join(segment.text for segment in segments)
                    print(full_text)
                    self.ducky_model.ask_ducky(full_text)

                    os.remove(tmpfile_path)
                except Exception as e:
                    print(f'Error processing audio: {e}')
                    continue
    '''
    def update_run_condition(self):
        self.run_condition = False

    def normalize(self, text):
        # Lowercase, remove punctuation, and extra spaces
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text)     # Replace multiple spaces with single space
        return text.strip()