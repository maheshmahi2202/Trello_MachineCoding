from Trello.models.card import Card

class CardService:
    def show_card(self, card_obj):
        output = {"id": card_obj.id, "name": card_obj.name, "description": card_obj.description,
                  "assigned_user": card_obj.assigned_user}
        return output

    def create_card(self, name):
        new_card = List()
        new_card.name = name
        return new_card