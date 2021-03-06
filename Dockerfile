# pull official base image
FROM python:3.9.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get -y install pipenv \
  && apt-get clean

# add app
COPY . .

# install python dependencies
RUN pipenv install --system --deploy --ignore-pipfile
