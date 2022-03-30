FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN  rm -Rf /var/lib/apt/lists/* && apt-get update && \
     pip3 install --no-cache-dir -r requirements.txt && \
     echo_supervisord_conf > /usr/src/app/supervisord.conf
COPY . .
CMD python3 manage.py migrate --settings config.prod && \
    supervisord
