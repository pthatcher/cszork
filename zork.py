import sys
import random

class Player:
    pass

class Bear:
    pass

you = Player()
you.location = "ground"
you.health = "healthy"
you.climb_count = 0

bear = Bear()
bear.health = "healthy"

while not you.health == "dead":
    if you.location == "pit":
        print "You are in a pit."
    if you.location == "ground":
        print "You are on the ground.  There is an bear."
        if bear.health == "healthy":
            print "The bear is healthy."
        elif bear.health == "wounded":
            print "The bear is wounded."
        elif bear.health == "dead":
            print "The bear is dead."
    if you.location == "forest":
        print "You are in the forest."
    if you.health == "healthy":
        print "You are healthy."
    if you.health == "crazy":
        print "You are insane."
    if you.health == "wounded":
        print "You are wounded."

    input = sys.stdin.readline().strip()

    if input == "climb with rope":
        if you.location == "pit":
            you.location = "ground"
        else:
            print "You can't climb here."
    elif input == "climb with ax":
        you.climb_count += 1
        if you.climb_count == 3:
            you.health = "dead"
        else:
            you.health = "wounded"
    elif input == "fight with ax":
        if you.location == "ground":
            outcome = random.choice(["win", "lose"])
            if outcome == "win":
                if bear.health == "wounded":
                    bear.health = "dead"
                    print "You beat the bear!"
                else:
                    bear.health = "wounded"
            elif outcome == "lose":
                if you.health == "wounded":
                    you.health = "dead"
                    print "You bear ate you!  At least you were tasty."
                else:
                    you.health = "wounded"
        else:
            print "You can't fight here."
    elif input == "run":
        if you.location == "pit":
            print "You bump your head on the wall"
            you.health == "wounded"
        elif you.location == "ground":
            if bear.health == "healthy":
                you.health = "dead"
                print "You bear ate you!  At least you were tasty."
            else:
                print "You escape!"
                you.location = "forest"
                
    else:
        you.health = "crazy"

print "You are dead.  You have failed your mission and your quest."
