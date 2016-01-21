from app import db


class Alternative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=True)

    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __repr__(self):
        return '<Alternative %r>' % self.text
