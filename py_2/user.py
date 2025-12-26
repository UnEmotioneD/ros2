class User:
    # class variable
    serial_number = 0

    # declare and initialize
    def __init__(self, name, email, password):
        # increase
        User.serial_number += 1
        # then assign
        self.member_id = User.serial_number  # instance variable
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        print(f"{self.name} login success")

    def __del__(self):
        print(f"{self.name} deconstructed")

    def send_email(self):
        print(f"Email sent to Mr.{self.name}")

    def input_password(self):
        return print("Enter password: ")

    def check_password(self) -> bool:
        password_input = self.input_password()

        if self.password is password_input:
            return True

        return False
