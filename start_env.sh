#!/bin/bash

echo "######## START FLASK DEV SERVER"
export FLASK_APP=wishingfish:WISHINGFISH
flask run

echo "######## GOT TO 'http://localhost:5000'"
