class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        miles = 0
    
    def displayinfo(self):
        print "This bike costs $", self.price, "This bike goes", self.max_speed, "and has", self.miles, "total miles"
    
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles = self.miles - 5
        if self.miles<0: 
            self.miles = 0
        return self

bike1=Bike(50, "5mph", 0)
bike2=Bike(150, "15mph", 0)
bike3=Bike(300, "30mph", 0)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()

