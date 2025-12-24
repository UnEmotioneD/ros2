class Member:
    member_count = 0

    def __init__(self, name, phone, address):
        Member.member_count += 1
        self.member_id = Member.member_count
        self.name = name
        self.phone = phone
        self.address = address

    def show_info(self):
        print(f"[회원 #{self.member_id}] {self.name}")
        print(f"연락처: {self.phone}")
        print(f"주소: {self.address}")

    def __del__(self):
        print(f"{self.name} 회원 정보 삭제")
