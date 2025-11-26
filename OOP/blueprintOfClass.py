class Rectangle:
    def __init__(self):
        self.length = 10
        self.breadth = 5

    def area(self):
        return self.length*self.breadth
    
    def paramatre(self):
        return 2*(self.breadth*self.length)

r = Rectangle()
print(r.area())
print(r.area)
print(r)