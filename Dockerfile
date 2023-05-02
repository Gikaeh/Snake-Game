# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

RUN pip3 install pytimedinput

COPY . .

CMD [ "python3", "main.py"]