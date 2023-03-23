FROM docker.io/python:3.8-buster
LABEL maintainer="Andrew Simonson <asimonson1125@gmail.com>"

WORKDIR /app
#ADD ./src /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/src

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
# CMD ["python3", "app.py"]
