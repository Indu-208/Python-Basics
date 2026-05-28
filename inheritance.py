class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    print("dog barks")
obj = Dog()
obj.sound()