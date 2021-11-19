from Trello.models.board import Board
from Trello.services.list_services import ListService
from Trello.services.user_services import UserService


class BoardService:
    board_details = {}

    def add_board(self, name):
        board = Board()
        board.set_name(name)

        self.__class__.board_details[board.id] = board
        return board

    def show_board(self, board_obj):
        output = {"id": board_obj.id, "name" : board_obj.name, "privacy": board_obj.privacy, "url": board_obj.url}
        output["cards"] = []
        for board_list in board_obj.lists:
            output["cards"].append(ListService.show_lists(board_list))

        output["members"] = []
        for member in board_obj.members:
            output["members"].append(UserService().show_user(member))
        return output

    def show_all_boards(self):
        for board in self.__class__.board_details:
            print(self.show_board(self.__class__.board_details[board]))

