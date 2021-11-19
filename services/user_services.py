from Trello.models.users import User


class UserService:
    user_details = {}

    def add_user(self, name, email):
        user = User()
        user.set_name(name)
        user.set_email(email)

        self.__class__.user_details[user.user_id] = user
        return user

    def show_user(self, user_obj):
        output={"name":user_obj.name, "email": user_obj.email}
        return output
