from basic_calculator import basic_calculator
import speech_recognition as sr

calc = basic_calculator()
r = sr.Recognizer()
val =0
with sr.Microphone() as source:
    audio_data = r.record(source, duration=4)
    text = r.recognize_google(audio_data)
    arr = text.split()
    if(arr[1] == '+'):
        val = calc.add(arr[0], arr[2])
    elif(arr[1] == '-'):
        val = calc.sub(arr[0], arr[2])
    elif(arr[1] == '*'):
        val = calc.multiply(arr[0], arr[2])
    elif(arr[1] == '/'):
        val = calc.divide(arr[0], arr[2])

    print(arr)
    