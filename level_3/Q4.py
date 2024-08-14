# Q4.py
class Shape:
    def __init__(self):
        self.name = "Shape"

    def area(self):
        return 0  # Default area

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = "Square"

    def area(self):
        return self.length * self.length

# Example usage
if __name__ == "__main__":
    square = Square(5)
    print(f"Area of the {square.name}: {square.area()}")
