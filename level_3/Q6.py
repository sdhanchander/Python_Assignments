# Q6.py
# Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Multiple Inheritance
class Father:
    def work(self):
        print("Father is working.")

class Mother:
    def cook(self):
        print("Mother is cooking.")

class Family(Father, Mother):
    def relax(self):
        print("Family is relaxing.")

# Multilevel Inheritance
class Grandparent:
    def wisdom(self):
        print("Grandparent's wisdom.")

class Parent(Grandparent):
    def job(self):
        print("Parent's job.")

class Child(Parent):
    def hobby(self):
        print("Child's hobby.")

# Example usage
if __name__ == "__main__":
    child = Child("Alice")
    child.greet()
    child.play()
    
    family = Family()
    family.work()
    family.cook()
    family.relax()

    grandchild = Child()
    grandchild.wisdom()
    grandchild.job()
    grandchild.hobby()
