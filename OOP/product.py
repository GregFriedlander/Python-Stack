class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        status = "for sale"
    
    def sell(self):
        if status != "for sale":
            status = "sold"
            print self.status
        return self
    
    def add_tax(self):
        tax = .15
        self.cost = self.cost + (self.cost * tax)
        return self
    
    def return_status(self):
        if self.status == "Defective":
            self.cost = 0
        elif self.status == "Open Box":
            self.cost = self.cost - .2
        return self

    def display_all(self):
        print "Price: $", self.cost
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost: $", self.cost
        print "Status:", self.status

toy=Product(20, "Lego", "10lbs", "Lego Brand", 10, "For Sale")
toy2=Product(20, "Lego", "10lbs", "Lego Brand", 10, "Defective")
toy3=Product(20, "Lego", "10lbs", "Lego Brand", 10, "Open Box")


toy3.return_status().add_tax().display_all()
