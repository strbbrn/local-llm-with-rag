#!/bin/bash

python3 -m pip install --upgrade pip
pip install -r requirements.txt

cat requirements.txt
echo "Shashi"
# Start Gunicorn server with your Flask application
gunicorn -b 0.0.0.0:80 -w 4 --timeout 600 app:app
