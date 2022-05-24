import smtplib
#from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import simpledialog
from RPA.Robocorp.Vault import Vault
application_window = tk.Tk()

mail= simpledialog.askstring("Input", "MailID?",parent=application_window)
password= simpledialog.askstring("Input", "Password", parent=application_window)
# secret = Vault().get_secret("Config")
# mail = secret['sender_email']
# password = secret['sender_password']
class SendEmail:
    #loading login credentials 
    def __init__(self):
        self.gmail_user = mail
        print(self.gmail_user)
        self.gmail_password =  password
        print(self.gmail_password)

    #for appple mail make changes here
    def create_msg(self,file,msg_html,subject,to_):
        self.to_=to_
        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = self.gmail_user
        msgRoot['To'] = self.to_
        #msgRoot['Bcc']= 'lokendra@propero.in'
        msgRoot['Subject'] = subject
        message =MIMEMultipart('alternative')
        message.attach(MIMEText(msg_html,_subtype='html'))
        msgRoot.attach(message)
        return msgRoot
    
    def send_mail(self,msgRoot,):
        #smtp.gmail.com
        with smtplib.SMTP_SSL('gsgp1032.siteground.asia', 465) as smtp:
            smtp.login(self.gmail_user, self.gmail_password) #Login to SMTP server
            to=[]
            to.append(self.to_)
            recipient=['lokendra@propero.in']
            #recipient=['18ucs169@lnmiit.ac.in']
            smtp.send_message(msgRoot, self.gmail_user,to+recipient)
            smtp.send_message(msgRoot, self.gmail_user,self.to_)
