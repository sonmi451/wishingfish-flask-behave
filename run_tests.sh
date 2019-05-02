#!/bin/bash

echo "######## RUNNING BEHAVE TESTS"
coverage run --omit */venv/* --source='.' -m behave

echo "######## GENERATING COVERAGE REPORT"
coverage html

echo "######## CHECK HTML REPORT at /wishingfish_flask_behave/htmlcov/index.html"
