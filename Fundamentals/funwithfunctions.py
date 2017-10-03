def odd_even():
    for i in range(1,2001): 
        if(i % 2 == 0):
            print "Number is ",i,".","This is an even number."
        if(i % 2 != 0):
            print "Number is ",i,".","This is an odd number."

# print odd_even()

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

# print multiply([2,4,10,16],5)

a = [2,4,10,16]
b = multiply(a,5)

print b

def layered_multiples():
    