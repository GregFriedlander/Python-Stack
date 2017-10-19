class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
    
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage 
        print "Tax:", self.tax


car1=Car(2000,"35mph", "Full", "15mpg")
car2=Car(2000, "5mph", "Not Full", "105mpg")
car3=Car(2000, "15mph", "Kind of Full", "95mpg")
car4=Car(2000, "25mpg", "Full", "25mpg")
car5=Car(2000, "45mph", "Empty", "25mpg")
car6=Car(20000000, "35mph", "Empty", "15mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()