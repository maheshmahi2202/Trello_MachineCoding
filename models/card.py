import uuid


class Card:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = None
        self.description = None
        self.assigned_user = "Unassigned"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def set_description(self,des):
        self.description = des

    def set_user(self, userobj):
        self.assigned_user = userobj

    def get_user(self):
        return self.assigned_user


