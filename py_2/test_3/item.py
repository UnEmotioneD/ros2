class Item:
    item_count = 0

    def __init__(self, name, price):
        Item.item_count += 1
        self.item_id = Item.item_count
        self.name = name
        self.price = price

    def show_info(self):
        print(f"[상품 #{self.item_id}] {self.name} - {self.price:,}원")

    def __del__(self):
        print(f"{self.name} 상품 정보 삭제")
