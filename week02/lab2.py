#Code Questions

import random

combatStrength = 100000000

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
weaponRoll = random.randint(1, 6)
if weaponRoll <= 2:
    print("You rolled a weak weapon friend..")
elif weaponRoll <= 4:
    print("Your weapon is meh..")
else:
    print("Nice weapon friend!")

if not weaponRoll == 1:
    print("At least it's not the fist...")

combatStrength += weaponRoll