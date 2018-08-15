# TODO:
#  *** Save game ***
#    important information:
#      number of trees
#      inventory
#      
#  chickens in the field by the log cabin hut and in tree house
#  eat banana
#  eat fish doesn't show an error
#  get tired if you chop down a tree
#  healthy of "tired"? (energy level?)
#  build a log cabin hut
#  go to the log cabin hut
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
#
# Bugs:
# - If you climb with an ax on the ground, you get hurt

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

class Supplies:
    pass

you = Player()
you.location = "pit"
# you.location = "clearing"  # ***
you.health = "healthy"

bear = Bear()
bear.health = "healthy"

forest = Forest()
forest.trees = 10

supplies = Supplies()
supplies.things = 3

inv = Inventory()
inv.ax = 0
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
inv.chicken = 0
inv.crowbar = 0
inv.armor = 0

def print_inventory():
    print "You have: "
    if inv.ax:
        print "  " + str(inv.ax) + " axes"
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
    if inv.chicken:
        print "  " + str(inv.chicken) + " chickens"
    if inv.armor:
        print "  " + str(inv.armor) + " armor"
    if inv.crowbar:
        print "  " + str(inv.crowbar) + " crowbars"
        

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
    elif you.location == "ground":
        print "You are on the ground.  There is a bear."
    elif you.location == "forest":
        print "You are in the forest."
    elif you.location == "clearing":
        print "You are in a clearing.  There is a log cabin hut in the middle.  There are chickens walking around."
    elif you.location == "roof":
        print "You are on the roof of a log cabin hut in a clearing."
    elif you.location == "treehouse":
        print "You are in a treehouse.  There are some supplies.  There are " + str(supplies.things) + " things in the supplies."
    else:
        print "you.location == '" + you.location + "'"

def print_your_health():
    if you.health == "healthy":
        print "You are healthy."
    elif you.health == "wounded":
        print "You are wounded."
    else:
        print "you.health == '" + you.health + "' state."

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
    elif you.location == "clearing":
        print "You are now on top of the log cabin hut."
        you.location = "roof"
    elif you.location == "roof":
        print "You try to climb an invisible wall, but fall off the roof and plow a tunnel through the ground all the way back to the pit."
        you.location = "pit"
        you_got_hurt()
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
    elif you.location == "clearing":
        print "You lasso the rope around the chimney and pull it down.  The man in the log cabin hut comes out and shoots you."
        you.location = "roof"
        # TODO: Random outcome of where he shot you.
        you_got_hurt()
    elif you.location == "roof":
        print "You climb down the chimney into a fire and are burned."
        # TODO: Random outcome of where he shot you.
        you_got_hurt()
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
    elif you.location == "clearing":
        print "You jump so far you land in the pit (???).  Too bad. So sad.  Have fun repeating all that stuff."
        you.location = "pit"
    elif you.location == "roof":
        print "You hop of the roof with no problem."
        you.location = "clearing"
    elif you.location == "treehouse":
        print "You jump so far you land in the pit (???).  Too bad. So sad.  Have fun repeating all that stuff."
    

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
    elif what == "banana":
        if inv.banana > 0:
            print "That was a good banana!"
            you_got_healed()
            inv.banana -= 1
        else:
            print "You don't have a banana!"
    
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
        print "You run into a clearing with a log cabin hut in the middle."
        you.location = "clearing"
    elif you.location == "clearing":
        print "You run back to the forest."
        you.location = "forest"
    elif you.location == "roof":
        print "You run across the air (you're magic!) but you land in the pit.  Don't press your luck."
        you.location = "pit"
    elif you.location == "treehouse":
        print "You run across the air (you're magic!) but you land in the pit.  Don't press your luck."
        you.location = "pit"


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
    elif you.location == "clearing":
        # TODO: Random outcome
        print "You chopped down the wheat of the owner of the log cabin hut.  He's not happy with you so he shot at you."
        you_got_hurt()
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
        
def grab():
    if you.location == "treehouse":
        if supplies.things < 1:
            print "There's nothing left.  You took it all, you selfish thief."
        else:
            supplies.things -= 1
            outcome = random.choice(["crowbar", "suite of armor", "ax"])
            print "You grabbed a " + outcome
            if outcome == "crowbar":
                inv.crowbar += 1
            elif outcome == "ax":
                inv.ax += 1
            elif outcome == "suite of armor":
                inv.armor += 1
            else:
                print "Nothing!!! Mwahahahahah"
    else:
        print "There's nothing to grab."

code_from_location_dictionary = {
    "ground": "g",
    "forest": "f",
    "clearing": "c",
    "treehouse": "t",
    "roof": "r",
    "pit": "p"
}

location_from_code_dictionary = {
    "g" : "ground",
    "f" : "forest",
    "c" : "clearing",
    "t" : "treehouse",
    "r" : "roof",
    "p" : "pit"
}

code_from_health_dictionary = {
    "healthy": "h",
    "wounded": "w",
    "dead": "d"
}

health_from_code_dictionary = {
    "h": "healthy",
    "w": "wounded",
    "d": "dead"
}

def save_game():
    name = "saved-game"
    file = open(name, "w")

    location_code = code_from_location_dictionary.get(you.location)
    file.write(location_code)

    health_code = code_from_health_dictionary.get(you.health)
    file.write(health_code)

    bear_health_code = code_from_health_dictionary.get(bear.health)
    file.write(bear_health_code)

    file.close()
    print "Saved to '" + name + "'"

def continue_game():
    name = "saved-game"
    file = open(name, "r")
    location_code = file.read(1)
    health_code = file.read(1)
    bear_health_code = file.read(1)

    you.location = location_from_code_dictionary.get(location_code)
    print_your_location()

    you.health = health_from_code_dictionary.get(health_code)
    print_your_health()

    bear.health = health_from_code_dictionary.get(bear_health_code)
    print_bear_health()

#    you.health = "what it was before"

#    forest.trees = "what it was before"    
#    bear.health = "what it was before"
#    inv = "what it was before"
#    print "Continuing game from '" + name + "'"
#    print "Your location is '" + you.location + "'"

shortcuts = {
    "l" : "look",
    "i" : "inventory",
    "d" : "dance",
    "cr" : "climb with rope",
    "co" : "cook",
    "ch" : "chop",
    "ca" : "climb with ax",
    "ea" : "eat apple",
    "eb" : "eat banana",
    "ebm" : "eat bear meat",
    "fa" : "fight with ax",
    "fs" : "fight with stone",
    "s" : "sleep",
    "h" : "help",
    "c" : "climb",
    "r" : "run",
    "j" : "jump",
    "g" : "grab",
    "ma" : "mine with ax",
    "z" : "continue",
    "s" : "save",
    "q" : "quit"
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
    "jump" : jump,
    "mine with ax" : ax_mining,
    "cook" : cook,
    "grab" : grab,
    "run" : run,
    "help" : help,
    "save" : save_game,
    "continue" : continue_game
}

print "Welcome to Zork.  You can ask for help (h)."
print_your_location()
while True:
    if you.health == "dead":
        print "******************************"
        print "*      You have died         *"
        print "******************************"
        break

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
    elif input == "quit":
        save_game()
        break
    else:
        print "That doesn't make sense."
