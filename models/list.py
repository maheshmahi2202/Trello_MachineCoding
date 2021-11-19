import uuid


class List:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = None
        self.cards = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_cards(self,cards):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def del_card(self,card):
        self.cards.remove(card)

    def delete_list(self):
        self.cards = []
        del self

