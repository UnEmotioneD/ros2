class Post:
    serial_num = 0

    def __init__(self, title, content, user):
        # each time object is constructed
        Post.serial_num += 1

        self.post_id = Post.serial_num
        self.title = title
        self.content = content
        self.user = user

    def show_info(self) -> None:
        print(f"[Post #{self.post_id}]", end=" ")
        print(self.title)
        print(self.content)
        self.user.show_info()

    def show_user(self) -> None:
        self.user.show_info()
