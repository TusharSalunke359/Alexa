import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#engine.say('I am your alexa')
#engine.say('What can I do you for you')

def talk(test):
    engine.say(test)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice= listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('i am fine what about you')
    elif 'are you single' in command:
        talk('yes i am single and ready to mingle')
    elif 'tell me jokes' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk('please say it again sometime my ears are not working hahahhaha ')

while True:
    run_alexa()