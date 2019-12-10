# periodic.py
from celery import Celery
app = Celery('periodic', broker='redis://h:pd6577324e1efbf5c3b5492b92cf36f5988db13e0ac1165c5e68c068012ac62a1@ec2-52-209-31-190.eu' \
                    '-west-1.compute.amazonaws.com:28369 ')
@app.task
def see_you():
    print("See you in ten seconds!")
app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 10.0
    }
}