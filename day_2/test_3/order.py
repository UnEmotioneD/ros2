class Order:
    order_count = 0

    def __init__(self, member):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.member = member  # Member 객체
        self.items = []  # Item 객체들을 담을 리스트

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} 상품이 주문에 추가되었습니다")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item_name} 상품이 주문에서 제거되었습니다")
                return
        print(f"{item_name} 상품을 찾을 수 없습니다")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_order(self):
        print(f"\n{'='*50}")
        print(f"[주문 #{self.order_id}]")
        print(f"주문자: {self.member.name} ({self.member.phone})")
        print(f"배송지: {self.member.address}")
        print(f"{'-'*50}")

        if len(self.items) == 0:
            print("주문 상품이 없습니다")
        else:
            print("주문 상품:")
            for item in self.items:
                print(f"  - {item.name}: {item.price:,}원")

        print(f"{'-'*50}")
        print(f"총 금액: {self.get_total():,}원")
        print(f"{'='*50}\n")

    def __del__(self):
        print(f"주문 #{self.order_id} 정보 삭제")
