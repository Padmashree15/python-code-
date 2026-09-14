import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
command = None

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vis' in command:
                command = command.replace('vis', '')
                print(command)
    except:
        pass
    return command


def run_vis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with Teagon Croft')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'where is' in command:
        place = command.replace('where is', '')
        info1 = wikipedia.summary(place,5)
        print(info1)
        talk(info1)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info2 = wikipedia.summary(thing, 10)
        print(info2)
        talk(info2)
    elif 'mine name' in command:
        talk('Your name is Maxx') 
    elif 'name' in command:
        talk('My name is vis and I am a self developing and learning software') 
    else:
        talk('Please say the command again.')


while True:
    run_vis()
