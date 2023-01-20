import os
from gtts import gTTS
from googletrans import Translator
from speech2text import text_var
#
trans = Translator()
#
w1 = text_var
#Init the translator as an object
sentence = trans.translate(w1, dest='hi')
#
tts = gTTS(sentence.text)
#
tts.save("output.mp3")
#
os.system("output.mp3")