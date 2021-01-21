FROM python:3.9-slim as driver

ENV GECKODIRVER_VERSION v0.29.0
ENV GECKODIRVER_URL https://github.com/mozilla/geckodriver/releases/download/${GECKODIRVER_VERSION}/geckodriver-${GECKODIRVER_VERSION}-linux64.tar.gz

RUN apt update \
    && apt install -y wget \
    && wget ${GECKODIRVER_URL} \
    && tar -xvf geckodriver-${GECKODIRVER_VERSION}-linux64.tar.gz


FROM python:3.9-slim as release

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONBUFFERED 1

COPY --from=driver /geckodriver /usr/local/bin/geckodriver

WORKDIR /app

RUN apt update \
    && apt install -y --no-install-recommends firefox-esr \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
    && adduser --disabled-password worker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

USER worker

ENTRYPOINT [ "celery" ]
CMD [ "-A", "src.celery", "worker", "--loglevel=INFO" ]
