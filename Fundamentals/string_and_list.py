words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day', 'month')

x = [2,54,-2,7,12,98]
print min(x) 
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]
new_list = [(y[0]),(y[-1])]
print new_list

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
first_list = z[:5]
second_list = z[5:]
print first_list
print second_list
second_list.insert(0, first_list)
print second_list