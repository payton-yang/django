FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN  rm -Rf /var/lib/apt/lists/* && apt-get update && \
     pip3 install --no-cache-dir -r requirements.txt && \
     echo_supervisord_conf > /usr/src/app/supervisord.conf && \
     mkdir /tmp/web && \
     touch /tmp/web/uwsgi.log  /tmp/web/uwsgi_err.log /tmp/web/celery.log /tmp/web/celery_err.log /tmp/web/celery_beat.log /tmp/web/celery_beat_err.log
COPY . .
CMD python3 manage.py migrate --settings config.prod && \
    supervisord
