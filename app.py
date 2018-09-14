from flask import Flask, render_template, request, logging, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/actions')
def actions():
    return render_template('actions.html')


@app.route('/listimages')
def listimages():
    return render_template('listimages.html')


@app.route('/listregistry')
def listregistry():
    return render_template('listregistry.html')


@app.route('/deleteimages')
def deleteimages():
    return render_template('deleteimages.html')


@app.route('/deleteregistry')
def deleteregistry():
    return render_template('deleteregistry.html')


if __name__ == '__main__':
    app.run(debug=True)
