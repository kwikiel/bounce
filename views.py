from app import app
from flask.ext.split import finished
from model import Alternative
from flask import render_template

@app.route('/')
def landing():
    al = Alternative.query.all()
    return render_template("index.html", al=al)


@app.route('/what')
def final():
    finished('headline')
    return "Thank for helping! Go back to work on your startup!"


@app.route('/nope')
def final2():
    finished('A')
    return "Thank for helping! Go back to work on your startup!"
