# print all the odd numbers from 1 to 1000
'''
oddnumbers = range(1,1000)
for i in oddnumbers:
    if i%2 != 0:
        print i 
'''
# print all multiples of 5 from 5 to 1,000,000
'''
list = range(5,1000000,5)
for i in list:
    print i
'''
# create a program that prints the sum of all the values in the list
'''
a = [1,2,5,10,225,3]
sum = 0


for i in a:
    sum += i
print sum
'''
# create a program that prints the average of the values in the list

x = [1,2,5,10,225,3]
sum = 0

for i in x:
    sum += i
avg = (sum/len(x))
print avg