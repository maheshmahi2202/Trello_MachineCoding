import uuid


class User:
    def __init__(self):
        self.user_id = str(uuid.uuid4())
        self.name = None
        self.email = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.user_id

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
