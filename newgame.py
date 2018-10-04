import sys 

class Place:
    pass

class Person:
    def alive(person):
        return person.health > 0
        
    def dead(person):
        return not person.alive()

tree = Place()
tree.name = "the tree"
tree.text = "You are by a very large tree."
tree.east = None
tree.north = None

cavern = Place()
cavern.name = "the cavern"
cavern.text = "You are in a dark cavern"
cavern.east = None
cavern.west = tree
cavern.north = None

castle = Place()
castle.name = "the castle"
castle.text = "You are in a large, spacious castle"
castle.east = None
castle.south = tree
castle.north = None

tree.north = castle
tree.east = cavern

# castle
# tree   cavern
#

you = Person()
you.location = tree
you.health = 10


def read():
    return sys.stdin.readline().strip()
    
while you.alive():
    print(you.location.text)
    input = read()
    if input == "east":
        if you.location.east:
            you.location = you.location.east
        else:
            print("You can't go east of %s." % (you.location.name,))
    elif input == "north":
        if you.location.north:
            you.location = you.location.north
        else:
            print("You can't go north of %s." % (you.location.name,))

