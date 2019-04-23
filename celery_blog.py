from celery import Celery
import requests
import time

app = Celery("celery_blog", broker="redis://localhost:6379/0")


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.url, resp.status_code)


def func(urls):
    for url in urls:
        fetch_url.delay(url)


URLS = [
    "http://www.google.com",
    "http://www.github.com",
    "https://amazon.in",
    "https://facebook.com",
    "https://twitter.com",
    "https://alexa.com",
]

func(URLS)
