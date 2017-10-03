test_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_characters(test_list, char):
   
    new_list = []
    for i in range(0, len(test_list)):
        if test_list[i].find(char) != -1:
            new_list.append(test_list[i])
    print new_list

        
find_characters(test_list, char)