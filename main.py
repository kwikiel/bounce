from app import app, finished, render_template
from models import Alternative


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
