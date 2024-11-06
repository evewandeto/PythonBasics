class Fruits: 
    # Constructor method
    def __init__(self, price, shape, name):
        self.price = price
        self.shape = shape
        self.name = name

    def display(self):
        print(f"My favourite fruit is {self.name}, it is {self.shape} in shape, and it costs {self.price}.")

# Create an instance of the class (object) outside the class definition
myobject = Fruits(20, "oval", "Banana")
myobject.display()