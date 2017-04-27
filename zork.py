# TODO:
#  do something in forest (like a maze with a clearing with a house with a guy that sells you things)
#  cook command
#  quit/die command?
#  money
#  a town
#  more efficient way to alter inventory randomly

import sys
import random
import time

class Player:
    pass

class Bear:
    pass

class Inventory:
    pass

you = Player()
you.location = "pit"
you.health = "healthy"

bear = Bear()
bear.health = "healthy"

inv = Inventory()
inv.ax = 1
inv.rope = 1
inv.stone = 0
inv.bear_skin = 0
inv.apple = 2
inv.bear_meat = 0


def print_inventory():
    print "You have: "
    if inv.ax:
        print "  " + str(inv.ax) + " ax"
    if inv.rope:
        print "  " + str(inv.rope) + " rope"
    if inv.stone:
        print "  " + str(inv.stone) + " stone"
    if inv.bear_skin:
        print "  " + str(inv.bear_skin) + " bear skin"
    if inv.bear_meat:
        print "  " + str(inv.bear_meat) + " bear meat"
    if inv.apple:
        print "  " + str(inv.apple) + " apple"
        

def print_actions():
    print "You can: "
    print "  look (l)"
    print "  inventory (i)"
    print "  run (r)"
    print "  eat (e)"
    if inv.ax > 0:
        print "  weave ax into rope"
    print "  sleep (s)"
    if you.location == "pit":
        print "  climb with rope (cr)"
        if inv.ax > 0:
            print "  climb with ax (ca)"
            print "  mine with ax (ma)"
    elif you.location == "ground":
        if inv.ax > 0:
            print "  fight with ax (fa)"
        print "  fight with stone (fs)"
        print "  jump into pit (j)"

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
    if inv.ax == 0:
        print "You don't have an ax."
        return

    you_got_hurt()
    if you.health == "dead":
        print "You fell and died.  I thought that by now you would learn that climbing with an ax is a bad idea."
    else:
        print "You fell and got wounded."
    

def ax_fighting():
    if inv.ax == 0:
        print "You don't have an ax."
        return

    if you.location == "ground":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            if bear.health == "wounded":
                print "You beat the bear!"
                bear.health = "dead"
                print "You gather up his skin and you chop him up into meat but he somehow flung you into the forest while you were doing so."
                you.location = "forest"
                inv.bear_skin += 1
                inv.bear_meat += 3
            else:
                print "A blow with the bear connected."
                bear.health = "wounded"
        elif outcome == "lose":
            you_got_hurt()
            if you.health == "dead":
                print "The bear ate you!  At least you were tasty."
            else:
                print "The bear slashed his claws at you!"
    else:
        print "You can't fight here."


def ax_mining():
    if inv.ax == 0:
        print "You don't have an ax."
        return

    if you.location == "pit":
        print "You received stone, but cut your finger."
        you_got_hurt()
        inv.stone += 1
    else:
        print "You can't mine here."

def stone_fighting():
    if inv.stone == 0:
        print "You imagine yourself throwing a stone."
    elif you.location == "ground":
        outcome = random.choice(["hit", "miss"])
        if outcome == "hit":
            if bear.health == "wounded":
                print "You nailed the bear!"
                bear.health = "dead"
                print "He dropped a bear skin and flung you into the forest."
                you.location = "forest"
                inv.bear_skin += 1
                inv.bear_meat += 1
            else:
                print "You hit the bear."
                bear.health = "wounded"
        elif outcome == "miss":
            print "You missed.  The bear is angry."
        inv.stone -= 1
    else:
        print "You hit yourself in the head with the stone."
        you_got_hurt()

def you_got_hurt():
    if you.health == "wounded":
        you.health = "dead"
    else:
        you.health = "wounded"

def you_got_healed():
    if you.health == "dead":
        pass
    else:
        you.health = "healthy"
    

def sleep():
    print "You are going into a deep sleep... dream world..."
    for _ in range(5):
        print "..."
        time.sleep(.1)

    outcome = random.choice(["stone stolen", "ax stolen", "nothing", "bear attack"])
    if outcome == "stone stolen":
        if inv.stone > 0:
            inv.stone -= 1
            print "A thief stole a stone!"
        else:
            print "You dreamt of a man stealing your stones.  But you have none."
    elif outcome == "ax stolen":
        if inv.ax > 0:
            inv.ax = 0
            print "A thief stole your ax!"
        else:
            print "You dreamt of a man stealing your ax.  But you have none."
    elif outcome == "nothing":
        print "Nothing was stolen.  Lucky you."
    elif outcome == "bear attack":
        if you.location == "pit":
            print "You dreamt of a bear attacking you."
        else:
            print "The bear got you while you're sleeping."
            you.health = "dead"
    you_got_healed()
    if you.health != "dead":
        print "You're awake!  Luckily, you're still alive."

def jump():
    if you.location == "pit":
        print "You can't jump out of a pit."
    elif you.location == "ground":
        print "You hit the ground painfully."
        you_got_hurt()
        you.location = "pit"

def eat(what):
    if what == "apple":
        if inv.apple > 0:
            you_got_healed()
            inv.apple -= 1
            print "You munched into the juicy apple and feel better." 
        elif inv.apple == 0:
            print "You imagine you're eating an apple.  But you don't really have one."
    elif what == "bear meat":
        if inv.bear_meat > 0:
            outcome = random.choice(["rotten", "delicious"])
            if outcome == "rotten":
                print "That meat was rotten.  Why did you eat it?"
                you_got_hurt()
            elif outcome == "delicious":
                print "You ate the bear and it was delicious.  You feel much better."
                you_got_healed()
            inv.bear_meat -= 1
        else:
            print "You imagine you're eating bear meat.  But you don't really have any."
    
def dance():
    print "You did a little jig."


shortcuts = {
    "l" : "look",
    "i" : "inventory",
    "d" : "dance",
    "cr" : "climb with rope",
    "ca" : "climb with ax",
    "ea" : "eat apple",
    "eb" : "eat bear meat",
    "ebm" : "eat bear meat",
    "fa" : "fight with ax",
    "fs" : "fight with stone",
    "h" : "help"
}

commands = {
    "dance" : dance,
    "inventory" : print_inventory,
    "climb with ax" : ax_climbing,
    "fight with ax" : ax_fighting,
    "fight with stone" : stone_fighting,
    "mine with ax" : ax_mining
}

print "Welcome to Zork.  You can ask for help (h)."
print_your_location()
while not you.health == "dead":
    input = sys.stdin.readline().strip()

    if input in shortcuts:
        input = shortcuts[input]
        # print "You used a shortcut!  You changed to " + input

    if input in commands:
        command = commands[input]
        command()
    elif input.startswith("eat"):
        if input.startswith("eat "):
            nothing, what = input.split(" ", 1)
            eat(what)
        else:
            print "Eat what?"
    elif input == "climb with rope":
        if you.location == "pit":
            you.location = "ground"
            print_your_location()
        else:
            print "You can't climb here."
    elif input == "help":
        print_actions()
    elif input == "look":
        print_your_location()
        print_your_health()
        if you.location == "pit":
            pass
        else:
            print_bear_health()
    elif input == "weave ax into rope":
        print "You cut yourself trying to bend a sharp piece of metal."
        you_got_hurt()
    elif input == "sleep" or input == "s":
        sleep()
    elif input == "jump" or input == "j":
        jump()
    elif input == "run" or input == "r":
        if you.location == "pit":
            print "You bump your head on the wall"
            you_got_hurt()
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

print "******************************"
print "*      You have died         *"
print "******************************"
