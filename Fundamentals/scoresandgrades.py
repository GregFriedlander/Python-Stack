def scores_and_grades():
    print "Scores and Grades"
    for i in range(0,10):
        import random
        random_num = random.randint(60,101)
        if random_num <= 100 and random_num >= 90:
            print "Score: ", str(random_num)+";", "Your grade is A"
        elif random_num <= 89 and random_num >= 80:
            print "Score: ", str(random_num)+";", "Your grade is B"
        elif random_num <= 79 and random_num >= 70:
            print "Score: ", str(random_num)+";", "Your grade is C"
        else:
            print "Score: ", str(random_num)+";", "Your grade is D"
    print "End of the programe. Bye!"

    
scores_and_grades()


# def scores_and_grades():
#     print "Scores and Grades"
#     for i in range(0,10):
#         import random
#         random_num = random.randint(60,101)
#         if random_num <= 100 and random_num >= 90:
#             print "Score: ", random_num,"; Your grade is A"
#         elif random_num <= 89 and random_num >= 80:
#             print "Score: ", random_num,"; Your grade is B"
#         elif random_num <= 79 and random_num >= 70:
#             print "Score: ", random_num,"; Your grade is C"
#         else:
#             print "Score: ", random_num,"; Your grade is D"
#     print "End of the programe. Bye!"

    
# scores_and_grades()


