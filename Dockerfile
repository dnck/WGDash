# base image
FROM python:3.8.0-slim as base_image
LABEL stage=wgdash_base_image
RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean

WORKDIR wgdash
COPY ./requirements.txt /wgdash/requirements.txt
COPY ./server.py /wgdash/server.py
COPY ./rss_man.py /wgdash/rss_man.py
COPY ./run.sh /wgdash/run.sh
COPY ./weather_man.py /wgdash/weather_man.py
COPY ./wsgi.py /wgdash/wsgi.py
COPY ./app.ini /wgdash/app.ini


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["run.sh"]
