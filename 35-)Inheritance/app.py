class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self):
        print("walk")

# Dont repeat your self


class Mammal:
    def walk(self):
        print("walk")


class _Dog(Mammal):
    def bark(self):
        print("bark")


class _Cat(Mammal):
    def be_cute(self):
        print("Mrr Mrrr")


dog1 = _Dog()
dog1.bark()

cat1 = _Cat()
cat1.be_cute()