FROM python:3.9.5-alpine
WORKDIR /py/src

COPY ./ ./

RUN apk add alpine-sdk
RUN apk add build-base libffi-dev

RUN python -m venv venv
RUN source venv/bin/activate

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt