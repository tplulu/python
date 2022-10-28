FROM python:3.9-slim

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
COPY . .

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 15400