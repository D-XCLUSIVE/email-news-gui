import smtplib, ssl
import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()

def send_email(message, reciever ):
    
    host = "smtp.gmail.com"
    port = 465

  
    username = config["EMAIL_USERNAME"]
    password = config["EMAIL_PASSWORD"]

   
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

