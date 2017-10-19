import datetime

class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id=id
        self.name=name
        self.number=number
        self.time=time
        self.reason=reason
    def display(self):
        printstr="\nID"+str(self.id)
        printstr+= "\nName"+str(self.name)
        printstr+= "\nNumber"+str(self.number)
        printstr+= "\nTime"+str(self.time)
        printstr+= "\nReason"+str(self.reason)
        print printstr


class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.size=len(self.calls)
    def add(self, call):
        self.calls.append(call)
        self.size=len(self.calls)
        return self

    def remove(self):
        self.calls.pop(0)
        self.size=len(self.calls)
        return self
    def removenum(self, number):
        for i in range(0, self.size):
            if self.calls[i].number==number:
                calltoPop=i
        self.calls.pop(calltoPop)
        self.size=len(self.calls)
        return self
    def info(self):
        for i in range(0,self.size):
            print self.calls[i].name+" "+self.calls[i].number
        print "Queue size:"+ str(self.size)
        return self

# now=datetime.datetime.now()
call1=Call("1","Patrick","555-222-1122", "5:38am", "Bill's too high")
call2=Call("2","Andy", "818-999-2829", "10:00am", "low bill")
call3=Call("3","Vlad", "818-944-9090", "9:00am", "tech issue")



cen1=CallCenter()

cen1.add(call1)
cen1.add(call2)
cen1.add(call3)

# cen1.info().remove().info()
cen1.removenum("818-999-2829").info()