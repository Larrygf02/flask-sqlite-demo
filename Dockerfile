FROM python:3.10

WORKDIR /usr/app

RUN apt update -y
RUN pip install --upgrade pip

RUN pip install uwsgi wheel
RUN pip install -r requirements.txt