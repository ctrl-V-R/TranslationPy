import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile('input.wav') as source:
    audio_data = r.record(source)
    text_var = r.recognize_google(audio_data)
    print(text_var)