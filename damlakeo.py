# s = input('Hay nhập số bất kỳ: ')
# print('Số vừa nhập là: ',s)

from random import randint

print("Chon Dam, La, Keo:"," ")
player = input()
computer = randint (0,2)
if computer == 0:
    computer = "Dam"
if computer == 1:
    computer = "La"    
if computer == 2:
    computer = "Keo"

print("You choose: ",player)
print("Computer chooses: ",computer)

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "Dam":
            print("Lose")
        else:
            print("Win")

    elif player == "Dam":
        if computer == "Keo":
            print("Win")
        else:
            print("Lose")

    elif player == "La":
        if computer == "Keo":
            print("Lose")
        else:
            print("Win")
    else:
        print("Nhap sai!")        