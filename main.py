import calendar
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia as wiki
import pyjokes
import webbrowser
import smtplib

listener = sr.Recognizer()  # Create a Recognizer object
engine = pyttsx3.init()
voice_rate = 175
engine.setProperty('rate', voice_rate)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def introduce():
    engine.say('Hello')
    engine.say('My name is Alexa your virtual assistant.')
    engine.say('What can I do for you today?')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        # Open Microphone and start recording audio
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print('You said :' + command)
    except Exception as e:
        print(e)
    return command


def take_command_without_activation():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except Exception as e:
        print(e)
    return command


def get_date():
    now = dt.datetime.now()
    my_date = dt.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December']
    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                       '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
                       '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th',
                       '29th', '30th', '31st']

    return 'Today is ' + month_names[monthNum - 1] + ' the ' + ordinal_numbers[dayNum - 1] + '.'


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz07@gmail.com', 'password')
    server.sendmail('xyz07@gmail.com', to, content)
    server.close()


def run_alexa():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        print('Playing' + song)
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command and 'what' in command:
        time = dt.datetime.now().strftime('%I.%M %p')
        print(time)
        talk('Current time is' + time)
   
    elif 'search' in command and 'wikipedia' in command:
        search = command.replace('search', '').replace('on', '').replace('wikipedia', '')
        info = wiki.summary(search, 1)
        print(info)
        talk(info)
    
    elif 'joke' in command and 'tell' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    
    elif 'date' in command:
        date = get_date()
        talk(date)
        print(date)
    
    elif 'send' in command and 'email' in command:
        try:
            talk("what should i send")
            content = take_command_without_activation()
            talk("Whom should i send it to?")
            to = take_command_without_activation()
            sendEmail(to, content)
            talk("Email has been sent to raj")
        except Exception as e:
            print(e)
    
    elif 'open google' in command:
        url = "google.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    
    elif 'open youtube' in command:
        url = "youtube.com"
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    
    else:
        talk('I am sorry I did not catch you.')
        talk('Could you say it again?')


# MAIN

introduce()
while True:
    run_alexa()
