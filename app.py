from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><p>Welcome to your Flask application!</p>'

@app.route('/about')
def about():
    return '<h1>About</h1><p>This is a simple Flask "Hello World" application.</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)