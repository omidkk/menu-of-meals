# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD [ "env", "FLASK_APP=start.py","python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=5001"]

EXPOSE 5001