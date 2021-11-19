from Trello.models.list import List


class ListService:
    def show_lists(self, list_obj):
        output = {}
        output["id"] = list_obj.id
        output["name"] = list_obj.name
        output["cards"] = list_obj.cards
        return output

    def create_list(self, name):
        new_list = List()
        new_list.name = name
        return new_list
