FROM python:3.9-alpine3.17 as python

WORKDIR /app

RUN apk update && apk add gcc postgresql-dev python3-dev rust

FROM python as serve

COPY ./ /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

FROM serve as dev

CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "80"]
