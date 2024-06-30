# Import Flask and other necessary modules
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return "Hello, World! This is my Flask application running with Gunicorn on port 80."

# Define a route for another URL
@app.route('/about')
def about():
    return "This is the about page."

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
