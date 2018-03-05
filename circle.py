class Circle() :

    pi = 3.14

    def __init__(self, radius) :
        self.radius = radius

    def area(self) :
        return (self.radius**2)*Circle.pi

    def set_radius(self, new_r) :
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.radius)
print(myc.area())
