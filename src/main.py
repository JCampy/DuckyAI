import sys
from PyQt6 import *
from PyQt6.QtWidgets import QApplication
from duck_window import RubberDuck
from ducky_ai_model import DuckyAIModel
from speech_to_text import SpeechToText
from text_to_speech import TextToSpeech
import threading

def main():
    app = QApplication(sys.argv) # Start gui 
    tts = TextToSpeech() # initialize tts
    ducky = DuckyAIModel(tts) # initialize open ai model
    spt = SpeechToText(ducky) # initialize spt
    window = RubberDuck(tts, ducky, spt) # load duck window

    # passing window to spt
    spt.rubber_duck_win = window
    window.show() # show the duck window

    print("starting thread")
    audio_thread = threading.Thread(target=spt.check_speech, daemon=True) # run capture audio in seperate thread
    audio_thread.start() # Start thread
    print("thread started")
    
    sys.exit(app.exec()) # Exit the application


if __name__ == "__main__":
    main()