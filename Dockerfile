FROM python:3.7-alpine

COPY requirements.txt /
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev                                                             
RUN pip install -r /requirements.txt

COPY src/speed_wrapper.py /etc/periodic/15min
RUN chmod 755 /etc/periodic/15min/speed_wrapper.py
WORKDIR /app

CMD ["sh", "-c", "tail -f /dev/null"]
