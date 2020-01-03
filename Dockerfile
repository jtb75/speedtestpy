FROM python:3.7-alpine

COPY requirements.txt /
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /requirements.txt
RUN apk del gcc

COPY src/* /app/
RUN chmod 755 /app/*
WORKDIR /app
ENTRYPOINT ["/app/speed_wrapper.py"]
