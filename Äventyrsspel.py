import random

print("""
""")

#  Klasser


class character:
    def __init__(self, hp, stre, lvl):
        self.hp = hp
        self.stre = stre
        self.lvl = lvl


class item:
    def __init__(self, item_name, item_stre, item_hp):
        self.item_name = item_name
        self.item_stre = item_stre
        self.item_hp = item_hp

class monster:
    def __init__(self, monster_name, monster_stre):
        self.monster_name = monster_name
        self.monster_stre = monster_stre


class trap:
    def __init__(self, trap_name, trap_stre):
        self.trap_name = trap_name
        self.trap_stre = trap_stre


#  Player

player = character(10, 0, 0)

#  Items

stone = item("Stone", 1, 0)
sword = item("Sword", 3, 0)
axe = item("Axe", 2, 0)
gold_ring = item("Gold Ring", 1, 1)
apple = item("Apple", 0, 2)
cake = item("Cake", 0, 3)

items = [stone, sword, axe, gold_ring, apple, cake]

#  Monster

cockroach = monster("Cockroach", 1)
bat = monster("Bat", 2)
goblin = monster("Goblin", 3)
orc = monster("Orc", 5)
minotaur = monster("Minotaur", 6)
giant = monster("Giant", 8)
dragon = monster("Dragon", 12)

easy_monsters = [cockroach, bat, goblin]
medium_monster = [orc, minotaur, giant]
boss = [dragon]

#  Trap

spike_trap = trap("Spike Trap", 2) 
poison_trap = trap("Poison Trap", 1)
boulder_trap = trap("Boulder Trap", 3)
fall_trap = trap("Fall Trap", 2")

traps = [spike_trap, poison_trap, boulder_trap, fall_trap]

# Värden för skada ska skjusteras senare
