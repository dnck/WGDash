# base image
FROM python:3.8.0-slim as base_image

MAINTAINER Dan Cook <cookdj0128@gmail.com>

RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean

WORKDIR .

RUN mkdir /WGDash

WORKDIR /WGDash

COPY ./requirements.txt /WGDash/requirements.txt
COPY ./wgdash.py /WGDash/wgdash.py
COPY ./rss_man.py /WGDash/rss_man.py
COPY ./run.sh /WGDash/run.sh
COPY ./weather_man.py /WGDash/weather_man.py
COPY ./wsgi.py /WGDash/wsgi.py
COPY ./app.ini /WGDash/app.ini

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD /WGDash/run.sh
