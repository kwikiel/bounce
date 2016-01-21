from flask import Flask
from flask import render_template
from flask.ext.split import split, finished
import os
import sys
import logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(64)
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
app.config['REDIS_URL'] = redis_url
app.register_blueprint(split)
app.config['SPLIT_DB_FAILOVER'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Debug
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


# Recursive import? Will it twerk?
class Alternative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=True)

    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __repr__(self):
        return "<ID: {0} Alternative {1}".format(self.id, self.text)


@app.route('/')
def landing():
    return render_template("index.html")


@app.route('/what')
def final():
    finished('cta')
    return "Thank for helping! Go back to work on your startup!"


@app.route('/nope')
def final2():
    finished('A')
    return "Thank for helping! Go back to work on your startup!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
