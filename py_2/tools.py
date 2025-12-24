def add(a, b):
    return a + b


def print_item(data):
    lst2 = []
    for item in data:
        lst2.append(f"For Mr.{item}.")
    return lst2


def count_item(data):
    count = 0

    for _ in data:
        count += 1

    return count
