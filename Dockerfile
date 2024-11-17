FROM python:3.11-slim

ENV PYHTONUNBUFFERED=1

WORKDIR /opt

COPY ./etc etc

RUN pip install -r etc/requirements.txt

COPY ./app app