#! /usr/bin/env bash

set -ex

export FLASK_APP=coffee

readonly IMAGE_NAME=mongodb

kill $(pgrep -f flask) || True
docker rm -f $(docker ps -aq) || True
docker build -t ${IMAGE_NAME} .
docker run -d -p 27017:27017 ${IMAGE_NAME}

pipenv run flask run
