# Part I

# def stars():
#     x = [4, 6, 1, 3, 5, 7, 25]
#     for i in range(0,len(x)):
#         x[i] = x[i] * ('*')
#         print x[i]

# stars()


# Part II

def stars():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for i in range(0,len(x)):
        if type(x[i]) == int:
            x[i] = x[i] * ('*')
            print x[i]
        elif type(x[i]) == str:
            x[i] = len(x[i]) * (x[i][0].lower())
            print x[i]

stars()
            
