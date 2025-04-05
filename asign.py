class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        return f"The {self.brand} {self.model} is now ON."

    def make_call(self, phone_number):
        return f"Calling {phone_number} on the {self.brand} {self.model}."

    def get_price(self):
        return f"The price of the {self.brand} {self.model} is ${self.price}."


# Creating an object of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", 999)

print(my_phone.turn_on())
print(my_phone.make_call("123-456-7890"))
print(my_phone.get_price())
