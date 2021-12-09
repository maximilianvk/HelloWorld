class Mammal:

    def __init__(self,animal):
        self.animal = animal

    def walk(self):
        print(f'{self.animal} likes to walk')


class Dog(Mammal):
    def bark(self):
        print('Bark')

class Cat(Mammal):
    def meow(self):
        print('Meow!')

dog = Dog('Dog')

dog.walk()
dog.bark()

cat = Cat('Cat')
cat.walk()
cat.meow()