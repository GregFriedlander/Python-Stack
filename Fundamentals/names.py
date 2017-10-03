# Part I

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def full_names(arr):
#     for x in arr:
#         print x['first_name'], x['last_name']

# full_names(students)

#Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(dic):
    count1 = 1
    count2 = 1
    print "Students"
    for key, data in users.items():
        if key == 'Students':
            for value in data:
                print count1, "-", value['first_name'], value['last_name'], "-", len(value['first_name']+value['last_name'])
                count1 += 1
    print "Instructors"
    for key, data in users.items():
        if key == 'Instructors':
            for value in data:
                print count2, "-", value['first_name'], value['last_name'], "-", len(value['first_name']+value['last_name'])
                count2 += 1

names(users) 



