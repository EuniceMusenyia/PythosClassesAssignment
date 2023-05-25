class Fruits():
    nutrient = "Vitamin C"

    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste

    def describe_fruit(self):
        return (f"The {self.color} {self.name} is {self.taste}")
    
    def flavour_of_fruit(self):
        return f"{self.name} is {self.taste}"
    
    def market_sales(self):
        return f"the market sells {self.name} at {self.price}"
    
