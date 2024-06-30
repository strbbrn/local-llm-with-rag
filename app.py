from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is Shashi."


@app.route('/about')
def about():
    return "This is the about page."

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
