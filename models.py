from app import db


class Alternative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiment = db.Column(db.String(500), unique=True)
    copy = db.Column(db.String(2500))

    def __init__(self, id, experiment, copy):
        self.id = id
        self.experiment = experiment
        self.copy = copy

    def __repr__(self):
        return "<Alt {0} {1} {2}>".format(self.id, self.experiment, self.copy)
