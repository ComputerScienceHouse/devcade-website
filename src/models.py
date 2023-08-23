class User:
    def __init__(self, uid, user_type, firstname, lastname, email, picture, admin):
        self.id = uid
        self.user_type = user_type
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.picture = picture
        self.admin = admin

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_json(self):
        return {"uid": self.uid,
                "user_type": self.user_type,
                "first": self.firstname,
                "last": self.lastname,
                "email": self.email,
                "picture": self.picture,
                "admin": self.admin}

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