import json
import apiai
import speech_recognition as sr


def speechRecognition():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("It's your cue")
        audio = recog.listen(source)
    i = True
    while i is True:
        try:
            text = recog.recognize_google(audio)
            i = False
            speechPrediction(text)
        except sr.UnknownValueError:
            print("Please speak again")
        except sr.RequestError:
            print("Please check your connection")


def speechPrediction(text):


    CLIENT_ACCESS_TOKEN = "6bcf8d38ee7344989af9aee9b0ffee11"
    DEVELOPER_ACCESS_TOKEN = "cae24c147f4d4af0b58ebbed1d97ad1b"

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    requests = ai.text_request()
    requests.query = text

    requests.lang = "en"
    response  = requests.getresponse()
    print(response)
    intent,room = JSONresponse(response)
    return intent,room

def JSONresponse(response):

    json_response = json.loads(response.read().decode('utf-8'))
    intent= []
    room= []
    print(json_response)
    print('...')

    result = json_response['result']
    intent = result['action']
    print(intent)

    room_result = result['parameters']
    room = room_result['room']
    print(room)
    return intent,room

#speechRecognition()
