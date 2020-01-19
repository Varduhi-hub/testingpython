class Smartphone:
    def setModel(self, model):
        self.model = model.lower()
    def getModel(self):
        return self.model
    def setOS(self, os):
        self.os = os.lower()
    def getOS(self):
        return self.os
    def setColor(self, model):
        self.color = color.lower()
    def getColor(self):
        return self.color
    def setPrice(self, price):
        self.price = price
    def getPrice(self):
        return self.price
        
my_smartphone = Smartphone()
my_smartphone.setModel("iPhone7")
my_smartphone.setOS("ios13")
my_smartphone.setPrice("500$")
specification_sheet = """
Model: {}
OS: {}
Price: {}
""".format(my_smartphone.getModel(), my_smartphone.getOS(), my_smartphone.getPrice())
print(specification_sheet)
