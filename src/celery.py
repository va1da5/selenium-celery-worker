from celery import Celery
from decouple import config
from . import services

CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_BACKEND_URL = config("CELERY_BACKEND_URL")

app = Celery("worker", broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)


@app.task
def get_rendered_html(*args, **kwargs) -> str:
    return services.get_rendered_html(*args, **kwargs)
