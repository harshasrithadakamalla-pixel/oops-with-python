class animal:
    def eat(self):
        print("animal eat food")
class dog(animal):
    def speak(self):
       print("dag bark")
d1=dog()
d1.eat()
d1.speak()