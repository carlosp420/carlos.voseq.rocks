FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y vim && rm -rf /var/lib/apt/lists/*

RUN apt-get autoremove -y
ADD requirements.txt /requirements.txt
RUN pip install pip --upgrade
RUN pip install -r /requirements.txt

COPY .env /code/.env

RUN mkdir -p /code
WORKDIR /code

ADD contact_syncer/. /code/
RUN ls /code

EXPOSE 8000
