from Trello.services.card_service import CardService
from Trello.services.user_services import UserService
from Trello.services.list_services import ListService
from Trello.services.board_service import BoardService

user1 = UserService().add_user("mahesh","immani.kumar@gmai.com")
user2 = UserService().add_user("Ravi", "ravi.kiran@gmail.com")

board1 = BoardService().add_board("board1")

print(BoardService().show_board(board1))

BoardService().show_all_boards()

board1.add_member(user1)
board1.add_member(user2)
print(BoardService().show_board(board1))

board1.remove_member(user1)
BoardService().show_all_boards()


list

