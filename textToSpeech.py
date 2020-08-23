# Import the required module for text
# to speech conversion
from gtts import gTTS
import os, string


# Language in which you want to convert

def text_to_speech(file_name='input', language='en', start_after_converting=False):
    language = language

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    with open(f"input/{file_name}", "r", encoding="utf-8") as i:
        text_inp = i.read().replace("\n", " ")

    output = gTTS(text=text_inp, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    output.save(f"output/{file_name}.mp3")

    # Playing the converted file
    if start_after_converting:
        os.system(f"start output/{file_name}.mp3")
