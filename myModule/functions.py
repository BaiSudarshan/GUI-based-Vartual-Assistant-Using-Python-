# for Command Line
import os
import datetime
import webbrowser
import wikipedia
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import smtplib
import urllib
from urllib.request import urlopen 


# for GUI
import tkinter as tk
from PIL import ImageTk,Image

#For Extracting Number
def extract_num(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append (float(t))
        except ValueError:
            pass
    return l

#For Calculation:
#Float to int if Possible
def f2i(number):  
    if (number-int(number))==0:
        return int(number)
    else :
        return number

def f_lcm(x):
    lcm=x[0]
    n=len(x)
    for i in range (n):
        if x[i]>lcm:
            lcm=x[i]
    d=1
    while (d!=0):
        d=0
        for i in range(n):
            d=d + lcm % x[i]
        lcm=lcm+1
    return "Your Answer is "+str(f2i(lcm-1))

def f_gcd(x):
    gcd=x[0]
    n=len(x)
    for i in range (n):
        if x[i]>gcd:
            gcd=x[i]
    d=1
    while (d!=0):
        d=0
        for i in range(n):
            d=d + x[i] % gcd
        gcd = gcd - 1
    return "Your Answer is "+str(f2i(gcd+1))

def f_add(x):
    n=len(x)
    sum=0
    for i in range(n):
        sum=sum+x[i]
    return "After Addition "+str(f2i(sum))

def f_sub(x):
    n=len(x)
    if n==2:
        return "After Subtraction"+str(f2i(x[0]-x[1]))
    else :
        return "Need 2 arguments, Got {} argumnet".format(n)

def  f_mul(x):
    n=len(x)
    mul=1
    for i in range(n):
        mul=mul*x[i]
    return "After Multiplication "+str(f2i(mul))

def f_div(x):
    n=len(x)
    if n==2:
        try:
            return 'Your answer is '+str(f2i(x[0]/x[1]))
        except ZeroDivisionError :
            return "Can not Divide by Zero"
    else :
        return "Need 2 arguments, Got {} argumnet".format(n)

operation={
        "PLUS":f_add,"ADD":f_add,"ADDITION":f_add,"SUM":f_add,"SUMMATION":f_add,
        "MINUS":f_sub,"SUBTRACT":f_sub,"SUB":f_sub,"SUBTRACTION":f_sub,"DIFFERENCE":f_sub,
        "PRODUCT":f_mul,"MULTIPLY":f_mul,"DIVIDE":f_div,"DIVISION":f_div,
        "LCM":f_lcm,"L.C.M":f_lcm,"LOWEST COMMON MULTIPLE":f_lcm,
        "GCD":f_gcd,"G.C.D":f_gcd,"GREATEST COMMON DIVISOR":f_gcd,"HCF":f_gcd,"H.C.F":f_gcd,"HIGHEST COMMON FACTOR" :f_gcd
        }
    
#for Internet
def is_net():
    try:
        urlopen("https://www.google.com",timeout=1)
        return True
    except Exception :
        return False

#For greetings
def greetings():
    d=int(datetime.now().hour)
    if  d>=0 and d<12 :
        return "Good Morning Sir"
    elif d>=12 and d<17 :
        return "Good Afternoon Sir"
    elif d>=17 :
        return "Good Evening Sir"

#for speaking
def speak(audio):
    e=pyttsx3.init()
    voices=e.getProperty("voices")
    e.setProperty("rate",130)
    e.setProperty("voice",voices[1].id)
    e.say(audio)
    e.runAndWait()
    return audio

#Listen me 
def speech_to_text():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        s.pause_threshold = 1
        s.energy_threshold = 1200
        s.operation_timeout = 3
        audio=s.listen(source)
    try:
        print("Recognizing....")
        text=(s.recognize_google(audio,language="en-in"))
        return (text)
    except sr.UnknownValueError :
        return "NoVoice"
 
    
#introduction
def introduce():
    return "I am Rajni and Your Assistant. I am here to help you"

#Send mail
def sendEmail(to,message):
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("babubai39894@gmail.com","dob591998")
        server.sendmail("babubai39894@gmail.com",to,message)
        server.close()
        return "Mail Sent Successfully"
    except Exception :
        return "Something Went Wrong"

def bye():
    h=datetime.now().hour
    if h<17:
        x="Have a Good Day Sir"
    else:
        x="Good Night Sir"
    return x

def lines(command):
    if "HY" in command or "HELLO" in command:
        return "Hi Sir, How can i help You ?"

    elif "TIME" in command or "DATE" in command:
        if "TIME" in command and "DATE" in command:
            dt1=datetime.now().strftime("%H:%M:%S")
            dt2=datetime.now().strftime("%d:%m:%Y")
            return "The Time is "+dt1+ " and Date is "+ dt2
        elif "TIME" in command : 
            dt=datetime.now().strftime("%H:%M:%S")
            return "The Time is "+dt
        elif "DATE" in command : 
            dt=datetime.now().strftime("%d:%m:%Y")
            return "The Date is "+ dt       

    elif "NAME" in command or "INTRODUCE" in command or "INTRODUCTION" in command or "WHO ARE YOU" in command or "ABOUT YOU" in command:
        return introduce()

    elif "HOW ARE YOU" in command or "YOU DOING" in command :
        return ("I am well, How may I help you SIR?")

    elif "WIKIPEDIA" in command :
        speak ("According to Wikipedia")
        command=command.replace("WIKIPEDIA","")
        result=wikipedia.summary(command,sentences=1)
        return result

    elif ("OPEN" in command or "RUN" in command) and ("YOU TUBE" in command or "YOUTUBE" in command):
        speak ("Openning Youtube, Please wait")
        webbrowser.open("https://www.youtube.com/")
        return "Youtube Opened"

    elif ("OPEN" in command or "RUN" in command)and "GOOGLE" in command:
        speak("Openning Google, please Wait")
        webbrowser.open("https://www.google.com/")
        return "Google Opened"

    elif ("OPEN" in command or "RUN" in command) and "MAIL" in command:
        speak("Openning Gmail, please Wait")
        webbrowser.open("https://www.gmail.com/")
        return "Gmail Opened"

    elif ("OPEN" in command or "RUN" in command) and "FACEBOOK" in command:
        speak ("Opening Facebook, Please Wait ...")
        webbrowser.open("www.facebook.com")
        return "Facebook Opened"

    elif ("PLAY" in command or "RUN" in command) and ("MUSIC" in command or "SONG" in command):
        #print(__file__)
        base=os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        #print(base)
        m_dir=os.path.join(base,"music")
        songs=os.listdir(m_dir)
        os.startfile(os.path.join(m_dir,songs[0]))
        return "Playing Music"

    else:
        print("Here")
        for i in command.split(" "):
            if i in operation.keys():
                num=extract_num(command)
                result = operation[i](num)
                return result
        else:
            return("Sorry I don't Understand")