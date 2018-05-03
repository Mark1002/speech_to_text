import speech_recognition as sr

recognizer = sr.Recognizer()
source_path = 'wav/333.wav'
with sr.AudioFile(source_path) as source:
    audio = recognizer.record(source)
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, language='zh-TW'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# cmu 經測試不佳
# try:
#     print("Sphinx thinks you said: {}".format(recognizer.recognize_sphinx(audio, language='zh-CN')))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")  
# except sr.RequestError as e:  
#    print("Sphinx error; {0}".format(e))
  