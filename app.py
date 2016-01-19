from flask import Flask
from flask import render_template
from flask.ext.split import split, finished
import os
import sys
import logging

app = Flask(__name__)
app.secret_key = os.urandom(64)
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
app.config['REDIS_URL'] = redis_url
app.register_blueprint(split)
app.config['SPLIT_DB_FAILOVER'] = True

# Debug
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def landing():
    return render_template("landing.html", options=["A", "B"])


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
