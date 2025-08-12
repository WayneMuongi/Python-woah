class Shape():

    def __init__(self,name):
        self.name=name

    def description(self):
        print(f"This shape is called",self.name) 


shape1=Shape(name="Circle")
shape1.description()

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.width=width
        self.length=length
        

r1=Rectangle(10,3)      
r1.description()

class area():
    def __init__(self,name):
        self.name=name

