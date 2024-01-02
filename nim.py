import random
from tokenize import Name

def main():
    StoneList=[]
    StonePile=random.randint(2,5)
    StoneQuantity=random.randint(1,9)
    Name=input("Enter Your name:")
    print("Hello ",Name,"! Welcome to the Game of Nim")
    player=Name
    Board(StoneList,StonePile,StoneQuantity,player)

def Board(StoneList,StonePile,StoneQuantity,player):
    #Print out the board
    for i in range(0,StonePile):
        StoneQuantity=random.randint(1,8)
        print("Pile {}:---{} Stones on this pile-----{}".format(i+1,StoneQuantity,'O'*StoneQuantity))
        StoneList.append(StoneQuantity)
    print("** 'O' represent stone **")
    
    CalculateNim(StoneList,StoneP
