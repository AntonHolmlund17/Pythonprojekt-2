import random

print(""" Welcome to the dungeon adventurer! Your goal is to survive through 12 levels. Each round you are going to have 3 options to choose from. 

1. Go to the next level
2. Check your stats
3. Look in your backpack

By going through to the next level you are going to choose one out of three doors. Behind each door there is a chance of finding a monster, falling in a trap or finding a chest with valuable items.""")


#  Klasser  ---------------------------------------

class character:
    def __init__(self, hp, stre, lvl):
        self.hp = hp
        self.stre = stre
        self.lvl = lvl

    def show_stats(self):
      player.stre = backpack_stre()
      print("\nYour stats are: ")
      print("HP:       " , self.hp)
      print("Strength: " , self.stre)
      print("Level:    " , self.lvl)


#  Item class ---------------------------------------

class item:
    def __init__(self, item_name, item_stre, item_hp):
        self.item_name = item_name
        self.item_stre = item_stre
        self.item_hp = item_hp



#  Monster class -----------------------------------

class monster:
    def __init__(self, monster_name, monster_stre):
        self.monster_name = monster_name
        self.monster_stre = monster_stre


#   Trap class -------------------------------------

class trap:
    def __init__(self, trap_name, trap_stre):
        self.trap_name = trap_name
        self.trap_stre = trap_stre


#  Player ------------------------------------

player = character(10, 0, 0)


#  Items -------------------------------------

stone = item("Stone", 1, 0)
sword = item("Sword", 3, 0)
axe = item("Axe", 2, 0)
gold_ring = item("Gold Ring", 1, 1)
apple = item("Apple", 0, 2)
cake = item("Cake", 0, 3)
empty = item("Empty", 0, 0)

items = [stone, sword, axe, gold_ring, apple, cake]

backpack = [empty, empty, empty, empty, empty,]

def backpack_stre():
  backpack_stre = 0
  for n in range(5):
    backpack_stre = backpack_stre + backpack[n].item_stre
  return backpack_stre
backpack_stre()


#  Monster -------------------------------------

cockroach = monster("Cockroach", 1)
bat = monster("Bat", 2)
goblin = monster("Goblin", 3)
orc = monster("Orc", 5)
minotaur = monster("Minotaur", 6)
giant = monster("Giant", 8)
dragon = monster("Dragon", 10)

early_monsters = [cockroach, bat, goblin]
middle_monsters = [goblin, orc, minotaur]
late_monster = [orc, minotaur, giant]


#  Trap ------------------------------------

spike_trap = trap("Spike Trap", 2) 
poison_trap = trap("Poison Trap", 1)
boulder_trap = trap("Boulder Trap", 3)
fall_trap = trap("Fall Trap", 2)

traps = [spike_trap, poison_trap, boulder_trap, fall_trap]

# Värden för skada ska skjusteras senare



#  Skriva felinput hantering
#  Kolla vs code för lösning på inventory

# Funktionen visar inventory

# Funktionen byter ut items i ryggsäcken
def swap(a, b):
    del backpack[b]
    backpack.insert(b, a)

# Funktion för att plocka upp item från kista och byta ut -------------------

def pick_up_item(item):
  show_backpack()

  player.hp = player.hp + item.item_hp
  
  print("\nWhat slot would you like to put this item in?")

  while True:
    slot = input(": ")
    if slot.isnumeric():
      slot = int(slot)
      if slot >= 1 and slot <= 5:
        swap(item, slot-1)  
        break
      else:
        print("\nPlease enter a number between 1 and 5\n")
    else:
      print("\nPlease enter a number between 1 and 5\n")
  player.stre = backpack_stre()
  

  
  

# Funktion för att visa backpack  ---------------------------------------

def show_backpack(): 
    print("\nYou take off your backpack and look inside. Inside you see:")
    print("\nNAME  STRENGTH  HP")
    for n in range(5):
        print(f"{backpack[n].item_name:12} {backpack[n].item_stre} {backpack[n].item_hp:3}")

    input(f"\nPress enter to continue")



# Funktionen ska fråga vad spelaren vill göra, inventory, backpack eller ett nytt rum. 

def first_choice(): 

  print("""


    What do you want to do? 
    1. Go to the next level 
    2. Check your stats     
    3. Look in your backpack""")

  while True:
    choice = input("\nWrite here: ")

    if choice == "1" or choice == "next level":
      return random_room()
    elif choice == "2" or choice == "stats":
      return player.show_stats()
    elif choice == "3" or choice == "backpack": 
      return show_backpack()
    else:
      return print("Wrong input, try again") 


# Fuktion för att slumpa monster ------------------

def monster():
  print(f"\n\n\nYou opened the door and found a monsters nest.") 

  
  if player.lvl <= 4:
    monster = random.choice(early_monsters)
  elif player.lvl <= 8:
    monster = random.choice(middle_monsters)
  elif player.lvl <= 12:
    monster = random.choice(late_monsters)

  print(f"\nYou have encountered a {monster.monster_name}!")
  input("\nPress enter to fight!")

  if player.stre >= monster.monster_stre:
    print("\nYou have defeated the monster without a sratch!")

  elif player.stre < monster.monster_stre:
    print("\nYou have lost some health!")
    player.hp = player.hp - monster.monster_stre + player.stre
    if player.hp > 0:
      print(f"\nYou have {player.hp} health left") 
    if player.hp <= 0:
      print(f"\nYou have 0 health left!")
    
  elif player.hp + player.stre <= monster.stre:
    print("\nThe monster defeated you!")
    player.hp = 0

#  Funktion för boss fighten -----------------------

def boss_fight():
  
  print(f"\nYou have encountered a {dragon.monster_name}!")
  input("\nPress enter to fight!")

  if player.stre >= dragon.monster_stre:
    print("\nYou have defeated the boss without a scratch! Wow you are        very strong") 
    print("\nCongratulations on winning the game!")
  
  elif player.stre < dragon.monster_stre:
    player.hp = player.hp - dragon.monster_stre + player.stre
    if player.hp <= 0:
      print(f"\nThe boss defeated you! You were not strong enough to defeat the boss.")
    print("\nBetter luck next time!")
  else:
    print("\nAfter a long and difficult fight you have managed to defeat the boss!")  
    print("\nCongratulations on winning the game!")


#  Funktion för att slumpa fälla ------------------

def trap():
  print("\n\n\nYou opened the door and found a trap") 
  trap = random.choice(traps)

  print(f"\nYou have encountered a {trap.trap_name}!")
  player.hp -= trap.trap_stre
  if player.hp > 0:
    print(f"\nYou have {player.hp} health left!")
  if player.hp <= 0:
    print(f"\nYou have 0 health left!") 


#   Funktion för att slumpa fram ett föremål ------

def item():
  print("\n \n \nYou opened the door and found a chest.")

  item = random.choice(items)
  print(f"\nYou have found a {item.item_name}!")

  choice = input("\nDo you want to pick it up? Yes or No: ")

  while choice.lower() != "yes"  and choice.lower() != "no":
    print("\nWrong input, try again.")
    print("\nPlease answer Yes or No")
    choice = input("\nDo you want to pick it up? Yes or No: ")

  if choice.lower() == "yes":
    pick_up_item(item)
  elif choice.lower() == "no":
    print("\nYou left the item behind.")


    # Funktion för att bestäma vad som är bakom dörren ---------- 

def room_choice(a):
    if a == 1:
      trap()
    elif a <= 3:
      monster()
    elif a <= 6:
      item()


#  Funktion som avgör vilket rum som ska öppnas ----------

def random_room():
  room_number = random.randint(1, 6)

  print("""
  In front of you there are 3 doors, behind one is a trap, the other is a chest and behind the third door is a monster. 
  Choose between door 1, 2 or 3.""") 

  door_choice = input("\nWhich door do you choose? ")

  while door_choice != "1" and door_choice != "2" and door_choice != "3": 
    print("Wrong input, try again") 
    door_choice = input("\nWhich door do you choose? ")

  room_choice(room_number)

# Kod som kör spelet

for round in range(1, 13):
  player.lvl = round
  if round > 1:
    print(f"\n\n\nYou have now reached round {round}! Well done!\n\n")
  first_choice()
  if player.hp <= 0:
    print("\nGame over, you lost")
    exit()
boss_fight()
