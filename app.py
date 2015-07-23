from flask import Flask
from flask import render_template, url_for
from flask.ext.split import split, finished
app = Flask(__name__)
app.register_blueprint(split)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SPLIT_DB_FAILOVER'] = True

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/what')
def final():
    finished('cta')
    return "Thank for helping! Go back to work on your startup!"

if __name__ == '__main__':
    app.run(debug=True)
