FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app

COPY ./requirments.txt /app/requirments.txt

RUN pip install -r requirments.txt

COPY . /app