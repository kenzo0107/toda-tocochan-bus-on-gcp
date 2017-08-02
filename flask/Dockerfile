FROM python:3.6.1-alpine
MAINTAINER Kenzo Tanaka

ENV WORK /app/

EXPOSE 5000

RUN mkdir $WORK
WORKDIR $WORK

ADD . $WORK
#COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
