from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

def play_audio(audio_file):
    os.system(f"start {audio_file}")

if __name__ == "__main__":
    text = "hi this is my 2nd version of text to speech using python,"
    audio_file = text_to_speech(text, lang='en')
    play_audio(audio_file)

