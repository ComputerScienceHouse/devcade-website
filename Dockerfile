FROM docker.io/python:3.8-buster
LABEL maintainer="Andrew Simonson <asimonson1125@gmail.com>"

WORKDIR /app
ADD ./src /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    apt-get -yq install libsasl2-dev libldap2-dev libssl-dev gcc g++ make && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/src

CMD [ "gunicorn", "-k" , "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "--bind", "0.0.0.0:8080", "application:app"]