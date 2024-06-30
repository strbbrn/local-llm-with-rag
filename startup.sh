#!/bin/bash



# Activate your Python virtual environment (if applicable)
# source /path/to/your/venv/bin/activate

# Install or update Python packages from requirements.txt
pip install -r requirements.txt

# Start Gunicorn server with your Flask application
gunicorn -b 0.0.0.0:80 -w 4 app:app
