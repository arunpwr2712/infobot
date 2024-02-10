import cv2
import numpy as np
import face_recognition
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import pyttsx3
import speech_recognition as sr 

import main as m


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
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


# Email credentials
sender_email = '20R21A6656@mlrinstitutions.ac.in'
sender_password = 'mlrit@123'
user_email = '20R21A6610@mlrinstitutions.ac.in'


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = user_email

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [user_email], msg.as_string())


# Function to send an email with an image attachment
def send_email_with_attachment(subject, body, image):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = user_email

    # Attach text body
    msg.attach(MIMEText(body, 'plain'))

    # Attach image
    image_attachment = MIMEImage(image)
    image_attachment.add_header('Content-Disposition', 'attachment', filename='visitor_image.jpg')
    msg.attach(image_attachment)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [user_email], msg.as_string())

# Load user's image and encode the face
user_image = face_recognition.load_image_file("images/known/arun.jpg")  # Replace with the user's image
user_encoding = face_recognition.face_encodings(user_image)[0]

# Initialize variables
visitor_information = []

# Function to handle visitor interaction
def handle_visitor(frame, face_locations):
    for (top, right, bottom, left) in face_locations:
        face_encoding = face_recognition.face_encodings(frame)[0]
        
        # Compare with the user's face
        results = face_recognition.compare_faces([user_encoding], face_encoding)

        if not any(results):
            # Visitor detected
            visitor_image = frame
            # visitor_image = frame[top:bottom, left:right]
            
            # Collect visitor information (photo, name, branch, purpose of visit)
            speak(" Visitor detected")
            speak(" Tell Your Name")
            visitor_name = listen()
            # visitor_name = input("Enter visitor's name: ")
            speak(" Tell Your Branch")
            visitor_branch = listen()
            # visitor_branch = input("Enter visitor's branch: ")
            speak(" Tell your purpose of visit")
            visitor_purpose = listen()
            # visitor_purpose = input("Enter purpose of visit: ")

            # Save visitor information
            visitor_information.append({
                'name': visitor_name,
                'branch': visitor_branch,
                'purpose': visitor_purpose,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            # Send an email to the user with visitor information and image attachment
            subject = "Visitor Detected!"
            body = f"Name: {visitor_name}\nBranch: {visitor_branch}\nPurpose: {visitor_purpose}"
            send_email_with_attachment(subject, body, cv2.imencode('.jpg', visitor_image)[1].tostring())

# # Initialize webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     # Find face locations in the frame
#     face_locations = face_recognition.face_locations(frame)

#     if face_locations:
#         handle_visitor(frame, face_locations)

#     # Display the frame
#     cv2.imshow("Visitor Tracking System", frame)

#     # Check for user input to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
















