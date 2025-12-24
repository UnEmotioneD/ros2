from post import Post
from user import User


def main() -> None:
    # User와 Post의 관계
    kim = User("김철수", "kim@email.com", "1234")

    post1 = Post("Python 기초", "클래스 공부중입니다", kim)
    post2 = Post("FastAPI 질문", "서버 구축 어렵네요", kim)

    post1.show_info()
    post2.show_info()
    # 출력 예시:
    # [게시글 #1] Python 기초
    # 내용: 클래스 공부중입니다
    # 작성자: 김철수 (kim@email.com)

    post1.show_user()
    # 출력: 작성자: 1 / 김철수


if __name__ == "__main__":
    main()
