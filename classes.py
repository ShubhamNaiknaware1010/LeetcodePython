class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

p1 = Person('John', 36) 
print(p1)
print(p1.age)