# Define the base class point
class point:
    # Define the constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Define the method set_cordinate(x,y)
    def set_cordinate(self, x, y):
        self.x = x
        self.y = y

# Define the new class new_point, which inherits the point class
class new_point(point):
    # Define the constructor
    def __init__(self, x=0, y=0, z=0):
        # Call the base class constructor
        super().__init__(x, y)
        self.z = z
