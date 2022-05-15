FROM --platform=linux/amd64 python:3.9.10-slim-buster
WORKDIR /usr/src
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /home/youdongknowme/requirements.txt
RUN apt-get -y update
RUN apt-get install -y wget xvfb unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN apt-get install -y build-essential libpq-dev
RUN pip install --upgrade pip