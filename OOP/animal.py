class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        # health = 0
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print "Health:", self.health
        return self

class Dog(Animal):
    health = 150
    # def __init__(self, name, health):
    #     # super(Dog, self).__init__(name, health)
    #     self.name = name
    #     self.health = health
    # return self
    
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "Health:", self.health, "I am a Dragon"
    


dr=Dragon("Pete", 170)
dr.fly().display_health()

# d = Dog("Max", 150)

# d.walk().walk().walk().run().run().display_health()












# pet=Animal("pet", 10)

# pet.walk().walk().walk().run().run().display_health()