from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/1')
def page_1():
	return 'page_1'

if __name__ == '__main__':
    app.run()