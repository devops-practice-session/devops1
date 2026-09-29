from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    # Running on 0.0.0.0 makes the app accessible externally
    app.run(host='0.0.0.0', port=3000)
