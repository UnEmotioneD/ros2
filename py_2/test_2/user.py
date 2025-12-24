class User:
    serial_num = 0

    def __init__(self, name, email, password):
        User.serial_num += 1

        self.user_id = User.serial_num
        self.name = name
        self.email = email
        self.password = password

    def show_info(self) -> None:
        print(f"Author: {self.name} ({self.email})")
