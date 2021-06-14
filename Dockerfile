FROM python:3.9.5-alpine

COPY ./ ./


RUN python -m venv venv
RUN source venv/bin/activate

RUN pip install --upgrade pip
# RUN pip install -r requirements.txt