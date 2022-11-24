# Pin version later
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt 

RUN pip install --no-cache-dir -r /requirements.txt 

RUN mkdir /app 
WORKDIR /app
COPY . /app

RUN adduser -D user 
USER user

ENTRYPOINT ["python", "bot.py"]