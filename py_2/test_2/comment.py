class Comment:
    serial_num = 0

    def __init__(self, comment, user, post):
        Comment.serial_num += 1
        self.comment_num = Comment.serial_num
        self.comment = comment
        self.user = user
        self.post = post

    def show_comment(self):
        print(f"[ Comment #{self.comment_num} {self.user.name}]")
        print("user info")
        self.user.show_info()
        print("post info")
        self.post.show_info()

    def notify_user(self):
        print(f"{self.user.user_id} / written by {self.user.name}")

    def __del__(self):
        print("Nice post! Comment removed.")
