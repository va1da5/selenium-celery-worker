from celery import Celery
from decouple import config
import argparse
import time

CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_BACKEND_URL = config("CELERY_BACKEND_URL")

app = Celery("client", broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)


def get_html(url):
    # The example script intentionally avoids importing actual task from src.celery.get_rendered_html
    # and utilizes Celery.send_task instead.
    result = app.send_task("src.celery.get_rendered_html", kwargs={"url": url})

    while not result.ready():
        print(result.state)
        time.sleep(1)

    print(result.get())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="URL", required=True)
    args = parser.parse_args()
    get_html(args.url)
