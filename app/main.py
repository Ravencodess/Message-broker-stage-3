from fastapi import FastAPI
from celery import Celery
from typing import Optional
from datetime import datetime
from tasks import send_mail
from fastapi.responses import PlainTextResponse


app = FastAPI()

def logger(event):
    with open("/var/log/messaging_system.log", "a") as log_file:
        log_file.write(f"{datetime.now()}: {event}\n")

@app.get("/")
def test(sendmail: Optional[str] = None, talktome: Optional[str] = None):
    response = {}

    if sendmail is not None:
        if sendmail == "":
            response["sendmail"] = f"no mail provided"
        else:
            logger(f"Sending mail to {sendmail}  .....")
            result = send_mail.delay(sendmail)
            logger(f"{result.get()}")
        response["sendmail"] = f"logged action to /logs"

    if talktome is not None:
        logger(talktome)
        response["talktome"] = f"logged action to /logs"

    if sendmail is None and talktome is None:
        response["Default"] = "no parameters provided"
    return response

@app.get("/logs")
def logs():
    with open("/var/log/messaging_system.log", "r") as log_file:
        log_content = log_file.read()
        return PlainTextResponse(content=log_content)
