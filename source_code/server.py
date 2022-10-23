'''
Created on Jan 10, 2017

@author: hanif
'''
import logging   
import string
import random

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


'''
This is the route for the short url, it will redirect to the original url, if the short url is not found, it will redirect to the 404 page
'''
@app.route('/r/<string:code>')
def r(code):
    data = db.read_code(code)
    if len(data) > 0 and len(data[0]) > 0:
        return redirect(data[0][2], code=302)

    return render_template('error.html')

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addshortcode', methods = ['POST', 'GET'])
def addshortcode():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form['url'], id_generator()):
            flash("A new Short Code has been added")
        else:
            flash("A new Short Code can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updateshortcode', methods = ['POST'])
def updateshortcode():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A Short Code has been updated')

        else:
            flash('A Short Code can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleteshortcode', methods = ['POST'])
def deleteshortcode():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A Short Code has been deleted')

        else:
            flash('A Short Code can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
