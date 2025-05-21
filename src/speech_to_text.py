import speech_recognition as sr
import faster_whisper
import tempfile
import os


class SpeechToText():

    def __init__(self, model):
        model_size = "large-v2" # model for whisper
        self.r = sr.Recognizer() # initializing recognizer
        # whisper model and run method
        print("model started")
        self.model = faster_whisper.WhisperModel(model_size, device="cpu", compute_type="int8")
        print("model running")
        self.run_condition = True
        self.ducky_model = model

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

    def update_run_condition(self):
        self.run_condition = False