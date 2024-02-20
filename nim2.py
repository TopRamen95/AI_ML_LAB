import random
from tokenize import Name

def main():
    StoneList=[]
    StonePile=random.randint(1,3)
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
    
    CalculateNim(StoneList,StonePile,player)


def Get_Input(StoneList,StonePile,player):
    while True:
            stones=input(player+",How many stones you want to remove? ")
            piles=input("Which pile you want to remove from? ")

            if(stones and piles)and(stones.isdigit()) and (piles.isdigit()):
                if(int(stones)>0) and (int(piles)>0) and (int(piles)<=len(StoneList)):
                    if(int(stones)<=StoneList[int(piles)-1]):
                        if(int(stones)!=0) and (int(piles)!=0):
                            break
            
            print("Invalid input, please try again")
    
    StoneList[int(piles)-1]-=int(stones)
    
    proceed(StoneList,StonePile,player)
    CalculateNim(StoneList,StonePile,player)

def proceed(StoneList,StonePile,player):
    print("Current Board:")
    for i in range(0,StonePile):
        print("Pile {}:---{} Stones on this pile-----{}".format(i+1,StoneList[i],"O"*StoneList[i]))
    print("** 'O' represent stone **")
    if(StoneList==[0]*len(StoneList)):
        print("Game Over, Bot Won. Thanks for playing!")
        exit()

def CalculateNim(StoneList,StonePile,player):
    nim=0
    for i in StoneList:
        nim=nim^i
    if(nim==0):
        #If Nim-Sum=0, Player start first
        Get_Input(StoneList,StonePile,player)
    else:
        #If Nim-Sum is not equal to 0, Bot start first
        BotTurn(StoneList,StonePile,player)


def BotTurn(StoneList,StonePile,player):
    print("BOT's TURN")
    nim=0
    for i in StoneList:
        nim=nim^i
    
    counter=0
    for i in StoneList:
        if((nim^i)<i):
            print("Bot take {} stone(s) from Pile {}".format(StoneList[counter]-(nim^i),counter+1))
            StoneList[counter]=(nim^i)

            break
        counter=counter+1  
    input("Press Enter to continue...")
    proceed(StoneList,StonePile,player)
    CalculateNim(StoneList,StonePile,player)


        
        
    
main()
