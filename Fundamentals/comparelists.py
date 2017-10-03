'''

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

'''

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "These lists are the same"
    else:
        print "These lists are not the same"

compare_lists(list_one, list_two)