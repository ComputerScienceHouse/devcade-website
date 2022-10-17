from init import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, uid, firstname, lastname, picture, admin):
        self.id = uid
        self.firstname = firstname
        self.lastname = lastname
        self.picture = picture
        self.admin = admin

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_json(self):
        return {"uid": self.uid,
                "first": self.firstname,
                "last": self.lastname,
                "picture": self.picture}

    def get_id(self):
        return self.id

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

db.create_all()