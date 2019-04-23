from celery import Celery
from time import sleep

app = Celery(__name__, broke="redis://localhost:6379/0")


@app.task
def add(x, y):
    sleep(5)
    return x + y


print(add(1, 2))
print("hello")
