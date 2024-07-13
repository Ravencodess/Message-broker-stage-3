from celery import Celery
from time import sleep
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import smtplib

load_dotenv()


celery = Celery(
    "tasks",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://"
)

@celery.task
def send_mail(email):
    email_sender = os.getenv("email_sender")
    email_password = os.getenv("email_password")
    email_receiver = email

    subject = "On the Road to Stage 4"
    body = "Send funds Prime Ejor"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, em.as_string())
        return f"Email sent to {email_receiver}"
    except Exception as e:
        return f"Failed to send email to {email_receiver}: {e}"
    
