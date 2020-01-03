FROM python:3.7-alpine

COPY requirements.txt /
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev                                                             
RUN pip install -r /requirements.txt
RUN apk del postgresql-dev gcc python3-dev musl-dev

COPY src/speed_wrapper.py /etc/periodic/15min
WORKDIR /app

CMD sleep 86400
