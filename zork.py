# TODO:
#  jump back in hole
#  don't allow negative stones
#  get more healthy somehow
#  do something in forest (like a maze with a clearing with a house with a guy that sells you things)
#  money
#  a town

import sys
import random

class Player:
    pass

class Bear:
    pass

class Inventory:
    pass

you = Player()
you.location = "pit"
you.health = "healthy"
you.climb_count = 0

bear = Bear()
bear.health = "healthy"

inv = Inventory()
inv.ax = 1
inv.rope = 1
inv.stone = 0
inv.bear_skin = 0

def print_inventory():
    print "You have: "
    if inv.ax:
        print "  " + str(inv.ax) + " ax"
    if inv.rope:
        print "  " + str(inv.rope) + " rope"
    if inv.stone:
        print "  " + str(inv.stone) + " stone"
    if inv.bear_skin:
        print "  " + str(inv.bear_skin) + "  bear skin"

def print_actions():
    print "You can: "
    print "  look (l)"
    print "  inventory (i)"
    print "  run (r)"
    print "  weave ax into rope"
    if you.location == "pit":
        print "  climb with rope (cr)"
        print "  climb with ax (ca)"
        print "  mine with ax (ma)"
    else:
        print "  fight with ax (fa)"
        print "  fight with stone (fs)"

def print_your_location():
    if you.location == "pit":
        print "You are in a pit."
    if you.location == "ground":
        print "You are on the ground.  There is an bear."
    if you.location == "forest":
        print "You are in the forest."

def print_your_health():
    if you.health == "healthy":
        print "You are healthy."
    if you.health == "wounded":
        print "You are wounded."

def print_bear_health():
    if bear.health == "healthy":
        print "The bear is healthy."
    elif bear.health == "wounded":
        print "The bear is wounded."
    elif bear.health == "dead":
        print "The bear is dead."

def ax_climbing():
    you.climb_count += 1
    if you.climb_count == 3:
        print "You fell and died.  I thought that by now you would learn that climbing with an ax is a bad idea."
        you.health = "dead"
    else:
        print "You fell and got wounded."
        you.health = "wounded"

def ax_fighting():
    if you.location == "ground":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            if bear.health == "wounded":
                print "You beat the bear!"
                bear.health = "dead"
                print "He dropped a bear skin and flung you into the forest."
                you.location = "forest"
                inv.bear_skin += 1
            else:
                print "A blow with the bear connected."
                bear.health = "wounded"
        elif outcome == "lose":
            if you.health == "wounded":
                print "The bear ate you!  At least you were tasty."
                you.health = "dead"
            else:

                print "The bear slashed his claws at you!"
                you.health = "wounded"
    else:
        print "You can't fight here."

def stone_fighting():
    if you.location == "ground":
        outcome = random.choice(["hit", "miss"])
        if outcome == "hit":
            if bear.health == "wounded":
                print "You nailed the bear!"
                bear.health = "dead"
                print "He dropped a bear skin and flung you into the forest."
                you.location = "forest"
                inv.bear_skin += 1
            else:
                print "You hit the bear."
                bear.health = "wounded"
        elif outcome == "miss":
            print "You missed.  The bear is angry."
        inv.stone -= 1
    else:
        print "You hit yourself in the head with the stone."
        if you.health == "wounded":
            you.health = "dead"
        else:
            you.health = "wounded"

def ax_mining():
    if you.location == "pit":
        print "You received stone, but cut your finger."
        if you.health == "wounded":
            you.health = "dead"
        else:
            you.health = "wounded"
        inv.stone += 1
    else:
        print "You can't mine here."

print "Welcome to Zork.  You can ask for help (h)."
print_your_location()
while not you.health == "dead":
    input = sys.stdin.readline().strip()

    if input == "climb with rope" or input == "cr":
        if you.location == "pit":
            you.location = "ground"
            print_your_location()
        else:
            print "You can't climb here."
    elif input == "help" or input == "h":
        print_actions()
    elif input == "look" or input == "l":
        print_your_location()
        print_your_health()
        if you.location == "pit":
            pass
        else:
            print_bear_health()
    elif input == "inventory" or input == "i":
        print_inventory()
    elif input == "climb with ax" or input == "ca":
        ax_climbing()
    elif input == "fight with ax" or input == "fa":
        ax_fighting()
    elif input == "fight with stone" or input == "fs":
        stone_fighting()
    elif input == "mine with ax" or input == "ma":
        ax_mining()
    elif input == "weave ax into rope":
        print "You cut yourself trying to bend a sharp piece of metal."  # *** make rope
        you.health == "dead"
    elif input == "run" or input == "r":
        if you.location == "pit":
            print "You bump your head on the wall"
            you.health == "wounded"
        elif you.location == "ground":
            if bear.health == "healthy":
                print "You bear ate you!  At least you were tasty."
                you.health = "dead"
                print_your_health()
            else:
                print "You escape!"
                you.location = "forest"
                print_your_location()
    else:
        print "That doesn't make sense."

print "You are dead.  You have failed your mission and your quest."
