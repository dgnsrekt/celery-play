import requests
import time


def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.url, resp.status_code)

    print("It took", time.time() - start, "seconds")


URLS = [
    "http://www.google.com",
    "http://www.github.com",
    "https://amazon.in",
    "https://facebook.com",
    "https://twitter.com",
    "https://alexa.com",
]

func(URLS)
