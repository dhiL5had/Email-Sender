from email import message
from json import load
from operator import le
import os
import ssl
import smtplib
from sys import exit

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class Mail:

    def __init__(self):
        self.email_sender= os.getenv("GMAIL")
        self.email_password= os.getenv("GMAIL_PASSWORD")

    def send_mail(self, receiver, subject, body):

        try:
            em= EmailMessage()
            em["From"]= self.email_sender
            em["To"]= receiver
            em["subject"]= subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, receiver, em.as_string())

        except Exception as err:
            print(err)

        finally:
            os.system("cls || clear")
            print("\nEmail sent successfully!")

class User_Selection:

    def display_selection(self):
        email_receiver = ""
        subject = ""
        body = ""
        choice = ""

        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
    
        email_receiver= input("\nEnter the recepient email-id: ")
        while email_receiver == '':
            print(LINE_UP, end=LINE_CLEAR)
            email_receiver= input("\nPlease enter the recepient email-id: ")

        choice= input("\nDo you want to update the email-id? (yes/no) ").lower()

        while choice not in ["y","n","yes","no"]:
            print(LINE_UP, end=LINE_CLEAR)
            choice= input("Do you want to update the email-id? (yes/no) ").lower()

        if choice in ["y","n","yes","no"]:

            subject= input("\nEnter Subject : ")
            while len(subject) == 0:
                print(LINE_UP, end=LINE_CLEAR)
                subject= input("\rPlease Enter a Subject : ")
            
            body= input("\nEnter the message body : ")
            while len(body) == 0:
                print(LINE_UP, end=LINE_CLEAR)
                body= input("Please enter the message body : ")

        mail= Mail()
        mail.send_mail(email_receiver, subject, body)
        
    
display= User_Selection()
display.display_selection()