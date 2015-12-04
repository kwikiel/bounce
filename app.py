from flask import Flask
from flask import render_template
from flask.ext.split import split, finished


app = Flask(__name__)
app.register_blueprint(split)
app.config['REDIS_URL'] = 'redis://dokku-redis-earn:6379/0'
# app.config['REDIS_IP'] = '172.17.0.53'
# app.config['REDIS_PORT'] = '32770'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
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
