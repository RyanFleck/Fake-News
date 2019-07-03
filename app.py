from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Its alive!'

if __name__ == '__main__':
    app.run()
