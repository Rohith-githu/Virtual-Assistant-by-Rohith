import os
try :
    import pyautogui
    from pyttsx3 import *
    try:
        import speech_recognition as sr
    except Exception as e :
        sp('Please check your internet connection.')
    import wikipedia
    import webbrowser
    import datetime
    import pywhatkit
    from pywhatkit.help import sendwhatmsg
    from requests.models import encode_multipart_formdata
    import practically
    import time
    from numberguessing import *
    import pyttsx3
    import os
    import webbrowser
except ModuleNotFoundError as e:
    print(e)
    os.system('pip install pyautogui')
    os.system('pip install pyttsx3')
    os.system('pip install SpeechRecognition')
    os.system('pip install wikipedia')
    os.system('pip install pywhatkit')
    os.system('pip install pipwin')
    os.system('pipwin install pyaudio')
