FROM python:3.10-slim-buster

RUN mkdir /opt/carford
WORKDIR /opt/carford

COPY requirements.txt requirements.txt
COPY . .


#RUN apt-get update
RUN pip install -r requirements.txt


CMD [ "python", "run.py"]
