class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item["price"]

        return total

store = Store("Python store")
store.add_item("apple",12.0)
store.add_item("grape",7.0)
print(store.stock_price())