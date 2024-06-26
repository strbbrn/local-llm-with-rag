from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, This is Shashi."


@app.route('/about')
def about():
    return "Hello from about page."

@app.route('/status')
def status():
    return jsonify({'status': True})

if __name__ == '__main__':
    app.run(debug=True)
