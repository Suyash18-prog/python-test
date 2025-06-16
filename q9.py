# Write a program to demonstrate method overloading using default arguments.
#inheriet same fuction

class Animal:
    def speak(self):
        print("All animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof WOOf!")

class Cat(Animal):
    def speak(self):
        print("meow meow !")


dog=Dog()
cat=Cat()
dog.speak()
cat.speak()