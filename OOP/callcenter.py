class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "ID: ", self.id
        print "Name: ", self.name
        print "Number: ", self.number
        print "Time: ", self.time
        print "Reason: ", self.reason

class Callcenter(object):
    def __init__(self):
        self.calls=[]
        self.size=len(self.calls)
    
    def add(self,call):
        self.calls.append(call)
        self.size=len(self.calls)
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.size=len(self.calls)
        return self

    def info(self):
        for i in range(0,self.size):
            print self.calls[i].name+" "+self.calls[i].number
        print "Queue Size: " + str(self.size)
        return self
    
    def removenumber(self, number):
        for i in range(0,self.size):
            if self.calls[i].number == number:
                calltopop = i
        self.calls.pop(calltopop)
        self.size=len(self.calls)
        return self
        

call1=Call("1", "Greg", "310-876-5432", "4:10pm", "Don't know where I am") 
call2=Call("2", "Marissa", "310-123-4567", "6:10pm", "Don't know where I am going") 
call3=Call("3", "Eddie", "808-999-6654", "9:30pm", "Don't know what it is") 

# call1.display()

cen1=Callcenter()

cen1.add(call1).add(call2).add(call3)

cen1.info().removenumber("310-123-4567").info()


