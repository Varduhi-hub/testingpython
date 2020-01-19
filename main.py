class Smartphone(object):
    def __init__(self, model, os, color, price):
        self.model = model
        self.os = os
        self.color = color
        self.price = price
    def show(self):
        print(self.name, self.os, self.color, self.price, )

my_smartphone = Smartphone("iphone7", "ios13", "black", "500$")
print(The values of my attributes are , "my_smartphone")


