from flask import Flask
from flask import render_template
from flask.ext.split import split, finished
import redis
import os


app = Flask(__name__)
app.register_blueprint(split)
app.config['REDIS_URL'] = redis.from_url(os.environ.get("REDIS_URL"))
app.secret_key = os.urandom(64)
app.config['SPLIT_DB_FAILOVER'] = True


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
