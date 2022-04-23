# rock paper scissors

import random
choice = ['rock','paper','scissors']
n = random.randint(0,2)
robot = choice[n]
# print(robot)
print("------rock paper scissors------")
print("choose: rock, paper,scissors")
player = input("You: ")
print("Robot:",robot)

if player=="rock":
    if robot=="rock":
        print(">>draw")
    elif robot =="paper":
        print(">>Robot win")
    else:   #scissors
        print(">>You win")
        
elif player=="paper":
    if robot=="rock":
        print(">>You win")
    elif robot =="paper":
        print(">>draw")
    else:   #scissors
        print(">>Robot win")
        
elif player=="scissors":
    if robot=="rock":
        print(">>Robot win")
    elif robot =="paper":
        print(">>You win")
    else:   #scissors
        print(">>draw")