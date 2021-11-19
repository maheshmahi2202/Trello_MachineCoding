import uuid


class Board:
    board_details = []

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = ""
        self.privacy = "PUBLIC"
        self.url = "www.machine-coding.com/board/" + str(self.id)
        self.members = []
        self.lists = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_url(self):
        return self.url

    def get_privacy(self):
        return self.privacy

    def set_privacy(self,privacy):
        self.privacy = privacy

    def add_member(self, user_obj):
        self.members.append(user_obj)

    def remove_member(self, member):
        self.members.remove(member)

    def get_members(self):
        return self.members

    def add_list(self, board_list):
        self.lists.append(board_list)

    def delete_list(self, board_list):
        self.lists.remove(board_list)

    def delete_board(self):
        self.lists=[]
        del self

