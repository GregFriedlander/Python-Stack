import random

def coin_toss():
    print "Starting the program..."
    headscount = 0
    tailscount = 0
    for i in range(1,5001):
        num = random.random()
        num_rounded = round(num)
        if num_rounded == 0:
            headscount+=1 
            print "Attempt", "#"+str(i)+":","Throwing a coin...", "It's a head!", "...", "Got "+str(headscount)+" head(s) so far and", str(tailscount)+" tail(s) so far"
        else:
            tailscount+=1
            print "Attempt", "#"+str(i)+":","Throwing a coin...", "It's a tail!", "...", "Got "+str(headscount)+" head(s) so far and", str(tailscount)+" tail(s) so far"
    print "Ending the program, thank you!"

coin_toss()