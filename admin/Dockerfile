FROM python:3.9-alpine3.17 as python

WORKDIR /app

RUN apk update && apk add gcc postgresql-dev python3-dev rust

FROM python as serve

COPY ./ /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

#EXPOSE 8001
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8001", "--noreload"]