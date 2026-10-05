from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Yaswanth! Welcome to DevOps Pipeline done !!!'

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
