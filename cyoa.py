import sys
import time

def read():
    return sys.stdin.readline().strip()
print "You are in a dark castle on a rainy night.  You hear the sound of wolves crying in the distance.  Should you stay [indoors] or go [outside]?"

dead = False

while not dead:
    input = read()

    if input == "indoors":
        print "A guy named Jeff with pizza says in a creepy voice 'hey, I got your delivery....."
        time.sleep(1)
        print "... it's Dominos'."
        print "You have two options: [eat] the pizza or let Jeff down and [ignore] the pizza."
        while not dead:
            input = read()
            if input == "eat":
                print "You eat the delicous pizza, but it's too hot and you burn your tongue and you die."
                dead = True
            elif input == "ignore":
                print "Jeff yells at you and storms out.  But he will return!"
                time.sleep(1)
                print "..."
                time.sleep(1)
                print "The pizza turns into a pizza monster and tries to eat you.  You can either [run] or [fight]."
                while not dead:
                    input = read()
                    if input == "run":
                        pass  # ...
                    elif input == "fight":
                        pass # ...
                    else:
                        print "You have to pick [fight] or [run].  You silly man."
            else:
                print "You have to pick [eat] or [ignore].  You silly man."
            
    elif input == "outside":
        print "The wolves eat you.  You die."
        dead = True
    else:
        print "You have to pick [indoors] or [outside].  You silly man."
    
