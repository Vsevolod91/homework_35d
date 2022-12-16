import csv


class Item:
    __pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.__pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, "r") as f:
            reader = csv.reader(f)
            count = -1
            for i in reader:
                count += 1
                if count == 0:
                    continue
                self = f"i{count}"
                name, price, quantity = i[0], i[1], i[2]
                self = cls(name, price, quantity)


    def __str__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__price}, {self.__quantity})"

if __name__ == "__main__":
    Item.instantiate_from_csv('items.csv')

    for item in Item.all:
        print(item)