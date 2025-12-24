from item import Item
from member import Member
from order import Order


def main() -> None:
    # 1. Member 생성
    member1 = Member("김철수", "010-1234-5678", "서울시 강남구")
    member2 = Member("이영희", "010-8765-4321", "서울시 서초구")

    member1.show_info()

    print("\n" + "=" * 50 + "\n")

    # 2. Item 생성
    item1 = Item("노트북", 1200000)
    item2 = Item("마우스", 30000)
    item3 = Item("키보드", 80000)
    item4 = Item("모니터", 350000)

    item1.show_info()
    item2.show_info()

    print("\n" + "=" * 50 + "\n")

    # 3. Order 생성 및 아이템 추가
    order1 = Order(member1)
    order1.add_item(item1)
    order1.add_item(item2)
    order1.add_item(item3)

    order1.show_order()

    # 4. 아이템 제거
    order1.remove_item("마우스")
    order1.show_order()

    # 5. 다른 회원의 주문
    order2 = Order(member2)
    order2.add_item(item4)
    order2.show_order()

    # 6. 데이터 흐름 확인
    print("\n[데이터 접근 예시]")
    print(f"주문1의 주문자: {order1.member.name}")
    print(f"주문1의 배송지: {order1.member.address}")
    print(f"주문1의 첫번째 상품: {order1.items[0].name}")
    print(f"주문1의 상품 개수: {len(order1.items)}개")


if __name__ == "__main__":
    main()
