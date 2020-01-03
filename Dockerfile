FROM python:3.7-alpine

COPY requirements.txt /
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev                                                             
RUN pip install -r /requirements.txt

COPY src/ /app
WORKDIR /app

CMD sleep 86400
