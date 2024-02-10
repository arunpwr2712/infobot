import threading
import cv2
import pyttsx3
import speech_recognition as sr  
import face_recognition
from datetime import datetime

import phrases as ph
import chatbot as cb
import face_recognize as l
import object as ob
import visitors as v

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(" "+audio)
    engine.runAndWait()

def listen():
    print("listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        return query
    except Exception as e:
        print(e)
        return listen()
    


object=""
def main():
    classNames,encodeListKnown=l.img_list()
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        face_locations = face_recognition.face_locations(img)
        print(face_locations)
        if len(face_locations)>0:

            img,isuser=l.face_main(success, img ,classNames,encodeListKnown)

            while isuser:
                question=listen()
                if question in ph.phrases:
                    img,object=ob.detect_and_find_middle_object(img)
                    response="Object is "+object
                elif question in ph.phrases_about_object:
                    response=cb.ask_chatbot(question+object)
                else:
                    response=cb.ask_chatbot(question)
                print(response)
                speak(response)

                
                success, img = cap.read()
                face_locations = face_recognition.face_locations(img)
                print(face_locations)
                img,isuser=l.face_main(success, img ,classNames,encodeListKnown)
                cv2.imshow('Video', img)


            else:
                v.handle_visitor(img,face_locations)



main()
