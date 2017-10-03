# l = ['magical unicorns',19,'hello',98.98,'world']

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def identify_list_type(l):
    sum = 0
    string = ""
    for i in l:
        if type(i) is int or type(i) is float:
            sum += i
        if type(i) is str:
            string += " " + i 
    if sum and string:
        print "This list you entered is of mixed type"
        print "Sum:", sum
        print "String:", string 
    elif sum:
        print "The list you entered is of integer type"
        print "Sum:", sum
    else:
        print "The list you entered is of string type"
        print "String:", string 

print identify_list_type(mixed_list)