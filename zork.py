# TODO:
#  eat banana
#  get tired if you chop down a tree
#  healthy of "tired"? (energy level?)
#  build a hut
#  go to the hut
#  sell stuff and get money
#  more stuff to do in treehouse
#  more health than 2
#  what happens when you run in the clearing?
#    chickens
#  fight bear with bare hands
#  fight with "bear" hands?
#  do something in forest (like a maze with a clearing with a house with a guy that sells you things)
#  quit/die command?
#  money
#  fight a tiger in the forest
#  dinosaurs in the clearing or town
#  a town
#  make a bow and arrow
#  more efficient way to alter inventory randomly

import sys
import random
import time

class Player:
    def have_wood(player):
        return inv.wood > 0

class Bear:
    pass

class Inventory:
    pass

class Forest:
    pass

you = Player()
you.location = "pit"
#  you.location = "forest"  # ***
you.health = "healthy"

bear = Bear()
bear.health = "healthy"

forest = Forest
forest.trees = 10

inv = Inventory()
inv.ax = 1
inv.rope = 1
# inv.stone = 2  # ***
inv.stone = 0
inv.bear_skin = 0
inv.apple = 2
# inv.bear_meat = 3  # ***
inv.bear_meat = 0
inv.roasted_bear_meat = 0
inv.wood = 0
inv.banana = 2

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
    if inv.roasted_bear_meat:
        print "  " + str(inv.roasted_bear_meat) + " roasted bear meat"
    if inv.apple:
        print "  " + str(inv.apple) + " apple"
    if inv.banana:
        print "  " + str(inv.banana) + " banana"
    if inv.wood:
        print "  " + str(inv.wood) + " wood"
        

def help():
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
    elif you.location == "forest":
        if inv.ax > 0:
            print "  chop (ch)"
        print "  climb (c)"
    elif you.location == "treehouse":
        if inv.ax > 0:
            print "  chop (ch)"

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

def climb():
    if you.location == "pit":
        print "You tried climbing with your hands, but it fails miserably."
        you_got_hurt()
    elif you.location == "forest":
        print "You find a treehouse laden with supplies."
        you.location = "treehouse"
    else:
        print "You can't climb here."

def climb_with_rope():
    if you.location == "pit":
        you.location = "ground"
        print_your_location()
    elif you.location == "forest":
        outcome = random.choice(["succeed", "fall"])
        if outcome == "fall":
            print "You tried climbing with the rope, but you fell and got hurt.  Try climbing with you bare hands next time."
            you_got_hurt()
        else:
            you.location = "treehouse"
    else:
        print "You can't climb here."

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
        if you.location == "ground":
            print "The bear got you while you're sleeping."
            you.health = "dead"
        else:
            print "You dreamt of a bear attacking you."
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
    elif what == "roasted bear meat":
        if inv.roasted_bear_meat > 0:
            print "That was delicious apple-roasted bear meat!  Your health improves"
            you_got_healed()
            you_got_healed()
            inv.roasted_bear_meat -= 1
        else:
            print "You imagine eating a juicy bear steak with apples.  But you don't have any."

    
def dance():
    print "You did a little jig."

def run():
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
    elif you.location == "forest":
        print "You run into a clearing with a hut in the middle."
        you.location = "clearing"

def chop():
    if you.location == "forest":
        if not forest.trees:
            print "You chopped down all the trees!  You swung and hit your leg."
            you_got_hurt()
        else:
            outcome = random.choice(["apple", "banana", "wood"])
            if outcome == "apple":
                print "You chopped down an apple tree and got apples and wood."
                inv.apple += 20 
                inv.wood += 10
            elif outcome == "banana":
                print "You chopped down a banana tree and got bananas and wood."
                inv.banana += 100
                inv.wood += 10
            elif outcome == "wood":
                print "You chopped down a tree and got lots of wood."
                inv.wood += 20
            else:
                print "What kind of tree was that??? " + outcome
            forest.trees -= 1
    elif you.location == "treehouse":
        print "You chopped down the tree you were in!  You die."
        you.health = "dead"
    else:
        print "There is no tree here.  You swung and it your leg."
        you_got_hurt()

def cook():
    if not you.have_wood():
        print "You need wood to cook on a fire."
    elif not inv.stone > 1:
        print "You need at least two stones to start a fire."
        you_got_hurt()
    elif inv.apple == 0:
        print "You can't roast bear meat without apples!"
    elif inv.bear_meat == 0:
        print "You wasted your apples roasting nothing."
        inv.apple -= 1
    else:
        print "You start a roasty fire using your wood and stones and cook your bear meat and apples"
        inv.bear_meat -= 1
        inv.apple -= 1
        inv.roasted_bear_meat += 1
        

shortcuts = {
    "l" : "look",
    "i" : "inventory",
    "d" : "dance",
    "cr" : "climb with rope",
    "co" : "cook",
    "ch" : "chop",
    "ca" : "climb with ax",
    "ea" : "eat apple",
    "eb" : "eat bear meat",
    "ebm" : "eat bear meat",
    "fa" : "fight with ax",
    "fs" : "fight with stone",
    "s" : "sleep",
    "h" : "help",
    "c" : "climb",
    "r" : "run",
    "ma" : "mine with ax"
}

commands = {
    "dance" : dance,
    "inventory" : print_inventory,
    "sleep" : sleep,
    "climb" : climb,
    "chop" : chop,
    "climb with ax" : ax_climbing,
    "fight with ax" : ax_fighting,
    "fight with stone" : stone_fighting,
    "mine with ax" : ax_mining,
    "cook" : cook,
    "run" : run,
    "help" : help
}

print "Welcome to Zork.  You can ask for help (h)."
print_your_location()
while not you.health == "dead":
    input = sys.stdin.readline().strip()

    if input in shortcuts:
        input = shortcuts.get(input)
        # print "You used a shortcut!  You changed to " + input

    if input in commands:
        command = commands.get(input)
        command()
    elif input.startswith("eat"):
        if input.startswith("eat "):
            nothing, what = input.split(" ", 1)
            eat(what)
        else:
            print "Eat what?"
    elif input == "climb with rope":
        climb_with_rope()
    elif input == "look":
        print_your_location()
        print_your_health()
        if you.location == "ground":
            print_bear_health()
        if you.location == "forest":
            print "There are " + str(forest.trees) + " trees."
    elif input == "weave ax into rope":
        print "You cut yourself trying to bend a sharp piece of metal."
        you_got_hurt()
    elif input == "jump" or input == "j":
        jump()
    else:
        print "That doesn't make sense."

print "******************************"
print "*      You have died         *"
print "******************************"
