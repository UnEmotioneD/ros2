from user import User


class UserService:
    def __init__(self):
        self.users = [
            User("Kim", "kim@naver.com", "1234"),
            User("Lee", "lee@naver.com", "5678"),
        ]

    def find_user(self, email):
        for user in self.users:
            if user.email is email:
                return user
        return None

    def login(self, email):
        user = self.find_user(email)

        if user is None:
            print("Cannot find the user")
            return False

        if user.check_password():
            print(f"{user.name} log in success")
            return True

        print("Wrong password")
        return False
