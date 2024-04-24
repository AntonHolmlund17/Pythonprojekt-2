import random

print(""" Welcome to the dungeon adventurer! Your goal is to survive through 12 levels. Each round you are going to have 3 options to choose from. 

1. Go to the next level
2. Check your stats
3. Look in your backpack
 
By going through to the next level you are going to choose one out of three doors. Behind each door there is a chance of finding a monster, falling in a trap or finding a chest with valuable items.""")


#  Klasser


class character:
    def __init__(self, hp, stre, lvl):
        self.hp = hp
        self.stre = stre
        self.lvl = lvl

    def show_stats(self):
      print("\nYour stats are: ")
      print("HP:      " , self.hp)
      print("Strength:" , self.stre)
      print("Level:   " , self.lvl)

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

# Backpack / inventory

backpack = ["", "", "", "", ""]

#  Items

stone = item("Stone", 1, 0)
sword = item("Sword", 3, 0)
axe = item("Axe", 2, 0)
gold_ring = item("Gold Ring", 1, 1)
apple = item("Apple", 0, 2)
cake = item("Cake", 0, 3)
empty = item("Empty", 0, 0)

items = [stone, sword, axe, gold_ring, apple, cake]
backpack = [empty, empty, empty, empty, empty,]

#  Monster

cockroach = monster("Cockroach", 1)
bat = monster("Bat", 2)
goblin = monster("Goblin", 3)
orc = monster("Orc", 5)
minotaur = monster("Minotaur", 6)
giant = monster("Giant", 8)
dragon = monster("Dragon", 12)

early_monsters = [cockroach, bat, goblin]
middle_monsters = [goblin, orc, minotaur]
late_monster = [orc, minotaur, giant]
boss = [dragon]

#  Trap

spike_trap = trap("Spike Trap", 2) 
poison_trap = trap("Poison Trap", 1)
boulder_trap = trap("Boulder Trap", 3)
fall_trap = trap("Fall Trap", 2)

traps = [spike_trap, poison_trap, boulder_trap, fall_trap]

# Värden för skada ska skjusteras senare

#  Skriva funktion för att slumpa rum
#  Skriva funktioner för vad som händer i varje rum
#  Skriva funktioner för att kunna visa ryggsäcken och spelarens stats
#  Skriva felinput hantering
#  Kolla vs code för lösning på inventory

# Funktionen visar inventory


def swap(item, slot):
    backpack.insert(slot, item)

def pick_up_item(item):
  print("This is what your backpack currently looks like")
  show_backpack()
  print("What slot would you like to put this item in?")
  slot = int(input(": "))
  while slot < 1 or slot > 5:
    print("Please enter a number between 1 and 5")
    slot = int(input(": "))

  swap(item, slot)
  
def show_backpack(): 
    print("\nNAME      STRE  HP")
    for n in range(5):
        print(f"{backpack[n].item_name:12} {backpack[n].item_stre} {backpack[n].item_hp:3}")



# Funktionen ska fråga vad spelaren vill göra, inventory, backpack eller ett nytt rum. 

def first_choice(): 
  
  while True:
    
    choice = input("""
    What do you want to do? 
    1. Go to the next level 
    2. Check your stats     
    3. Look in your backpack
    
    Write here: """)
    
    if choice == "1" or choice == "next level":
      return random_room()
    elif choice == "2" or choice == "stats":
      return player.show_stats()
    elif choice == "3" or choice == "backpack": 
      return show_backpack()
    else:
      return print("Wrong input, try again") 



def monster():
  if player.lvl <= 4:
    monster = random.choice(early_monsters)
  elif player.lvl <= 8:
    monster = random.choice(middle_monsters)
  elif player.lvl <= 12:
    monster = random.choice(late_monsters)

  print(f"\nYou have encountered a {monster.monster_name}!")
  input(f"Press enter to fight!")
  
  if player.stre >= monster.monster_stre:
    print("\nYou have defeated the monster and didn't lose any health!")
  elif player.stre < monster.monster_stre:
    print("\nYou have lost some health!")
    player.hp -= monster.monster_stre - player.stre
    print(f"\nYou have {player.hp} health left!")
  elif player.hp + player.stre <= monster.stre:
    print("\nThe monster defeated you!")
    player.hp == 0
    
    
    

def trap():
  trap = random.choice(traps)
  print(f"\nYou have encountered a {trap.trap_name}!")
  player.hp -= trap.trap_stre
  print(f"\nYou have {player.hp} health left!")


def item():
  item = random.choice(items)
  print(f"\nYou have found a {item.item_name}!")
  
  while True:
    choice = input("\nDo you want to pick it up? Yes or No: ")
    if choice.lower() == "yes":
      pick_up_item(item)
    elif choice.lower() == "no":
      print("\nYou left the item behind.")
      break
    else:
      print("\nWrong input, try again.")
    
  
def room_choice(a):
    if a == 0:
      monster()
    elif a == 1:
      trap()
    elif a == 2:
      item()

  
def random_room():
  room_number = random.randint(0, 3)
  print("""
  In front of you there are 3 doors, behind one is a trap, the other is a chest and behind     the third door is a monster. 
  Choose between door 1, 2 or 3.""")  
  door_choice = int(input("\nWhich door do you choose? "))
  if door_choice > 3:
      print("Wrong input, try again") 
  room_choice(room_number)


# Kod som kör spelet

first_choice() 




  
  
