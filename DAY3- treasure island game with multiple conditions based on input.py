print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("you're at a cross road. where do you want to go? ")
road=input("Type 'left' or 'right'\n").lower()
if road=="left":
    print("you've come to a lake.There is an island in the middle of the lake.")
else:
    print("you've fall into a hole. \n GAME OVER")
wait=input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
if wait=="wait":
    print("you arrive at the island unharmed . There is a house with 3 doors .\n one red, one yellow and one blue.")
    door=input("Which colour do you choose?\n").lower()
    if door=="red":
        print("you are burned by fire.\n GAME OVER")
    elif door=="blue":
        print("you are eaten by beasts.\n GAME OVER")
    elif door=="yellow":
        print("you got the treasure.\n YOU WIN")
    else:
        print("you choose the wrong input")
else:
    print("you are attacked by trout.\n GAME OVER")
