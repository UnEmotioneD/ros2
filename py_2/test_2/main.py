from user import User
from post import Post
from comment import Comment


def main() -> None:
    kim = User("김철수", "kim@email.com", "1234")
    lee = User("이영희", "lee@email.com", "5678")

    post1 = Post("Python 기초", "클래스 공부중입니다", kim)
    post2 = Post("FastAPI 질문", "서버 구축 어렵네요", lee)

    comment1 = Comment("좋은 글이네요!", kim, post1)
    comment2 = Comment("도움이 되었습니다", lee, post2)

    comment1.show_comment()

    print()

    comment2.show_comment()
    # 출력 예시:
    # [댓글 #1] 김철수: 좋은 글이네요!

    print()

    comment1.notify_user()
    # 출력: 1 / 김철수님이 댓글을 작성했습니다

    print()

    del comment1
    del comment2
    # 출력: 좋은 글이네요! 댓글 삭제


if __name__ == "__main__":
    main()
