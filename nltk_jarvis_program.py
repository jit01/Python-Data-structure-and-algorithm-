import datetime
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print([i.id for i in voices])
engine.setProperty('voice', voices[11].id)


def talk(statement):
    engine.say(statement)
    engine.runAndWait()


def start():
    time = int(datetime.datetime.now().hour)
    if 0 <= time < 12:
        talk("Good Morning!")
    elif 12 <= time < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("Jarvis is activated. Please tell me how may help you ")


def getcommand():
    re = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = re.listen(source, timeout=3, phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = re.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        print(str(e))

        print("Please say that again...")
        return "None"

    return query


if __name__ == "__main__":
    start()
    while True:
        query = getcommand().lower()
        try:
            # if 'Hi' or 'Hello' in query:
            #     talk("Hi I'm Jarvis! How Can I help you ")
            if 'wikipedia' in query:
                talk("Searching in wikipedia")
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                talk("According to Wikipedia")
                talk(results)
            elif 'open youtube' in query:
                webbrowser.open('youtube.com')
        except Exception as e:
            print(str(e))

            talk("Didn't found that, could you please say it again")

