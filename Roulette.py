import random
import pandas as pd
from colorama import Fore
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

def spin(betLimit,balance,bet,betNum):
    if bet > betLimit:
        bet=betLimit
    elif bet < 1:
        bet = 1
    
    result = random.randint(0,37)
    print("The result was "+str(result)+".")
    if betNum.isdigit():
        if result == int(betNum):
            print("You Win!!")
            balance+= 35*bet
            
        else:
            print("You lose. Try again.")
            balance -= bet
    if betNum == "BLACK":
        if result in black:
            print("You Win!!")
            balance += bet
        else:
            print("You lose. Try again.")
            balance -= bet
            
    elif betNum == "RED":
        if result not in black:
            print("You Win!!")
            balance+= bet
        else:
            print("You lose. Try again.")
            balance -= bet
            
    return balance
        
print("Welcome to the Roulette Table.Place your bet and hope you get lucky.")
print("A single number bet pays 35 to 1. Betting on a colour pays even money.")

email = ""
validEmail = False
while not validEmail:
    email = input("Game results will be logged under a user email for security.Please enter a valid email:")
    if email.count("@")==1 and email.count(".")>0:
        validEmail = True
        
    
scoreCard = input("Enter a title for your score card,which will record the results of your game:")+".csv"
gameMode = input("Which game mode do you want to play:SINGLEPLAYER/MULTIPLAYER/SIMULATION:").upper()

yourBalance = 0
houseBalance = 0
rounds = [1000,2000,3000,4000,5000]



if gameMode == "SINGLEPLAYER":
    scoreCardFile = open("singleplayer\\"+scoreCard,"w",newline="")
    dataDict = {
        "Bet Limit":[],
        "Balance":[],
        "Bet":[],
        "Payout":[],
        "New Balance":[],
        "Email":[email]}
    for value in rounds:
        oldBalance = yourBalance
        currentBetLimit = value
        print("Your balance is "+str(yourBalance)+".")
        currentBet = int(input("How many chips are you betting?(between 1 and "+str(currentBetLimit)+"):"))
        currentBetNum = input("What numbers are you betting on? BLACK,RED or any number between 1 and 36:").upper()
        print("-----------------------------------------------------------------")
        yourBalance = spin(currentBetLimit,yourBalance,currentBet,currentBetNum)
        print("-----------------------------------------------------------------")
        payout = yourBalance - oldBalance
        dataDict["Bet Limit"].append(currentBetLimit)
        dataDict["Balance"].append(oldBalance)
        dataDict["Bet"].append(str(currentBet)+","+str(currentBetNum))
        dataDict["Payout"].append(payout)
        dataDict["New Balance"].append(yourBalance)
        
    resultDataFrame = pd.DataFrame(dataDict,index = range(1,6))
    resultDataFrame.index.name = "Round"
    print(resultDataFrame)
    resultDataFrame.to_csv(scoreCardFile)
        
        
    scoreCardFile.close()
    
if gameMode == "MULTIPLAYER":
    scoreCardFile = open("multiplayer\\"+scoreCard,"w",newline="")
    players = [["Player 1",yourBalance],["Player 2",houseBalance]]
    dataDict = {
        "Bet Limit":[],
        "P1 Balance":[],
        "P1 Bet":[],
        "P1 Payout":[],
        "P1 New Balance":[],
        "P2 Balance":[],
        "P2 Bet":[],
        "P2 Payout":[],
        "P2 New Balance":[],
        "Email":[email]}
    
    for value in rounds:
        currentBetLimit = value
        dataDict["Bet Limit"].append(currentBetLimit)
        print(Fore.BLUE)
        for profile in players:
            print(profile[0]+"'s balance is "+str(profile[1])+".")
            oldBalance = profile[1]
            currentBet = int(input("How many chips are you betting?(between 1 and "+str(currentBetLimit)+"):"))
            currentBetNum = input("What numbers are you betting on? BLACK,RED or any number between 1 and 36:").upper()
            print("-----------------------------------------------------------------")
            profile[1]=spin(currentBetLimit,oldBalance,currentBet,currentBetNum)
            print("-----------------------------------------------------------------")
            payout = profile[1]-oldBalance
            if profile[0] == "Player 1":
                dataDict["P1 Balance"].append(oldBalance)
                dataDict["P1 Bet"].append(str(currentBet)+","+str(currentBetNum))
                dataDict["P1 Payout"].append(payout)
                dataDict["P1 New Balance"].append(profile[1])
                print(Fore.RED)
                
            else:
                dataDict["P2 Balance"].append(oldBalance)
                dataDict["P2 Bet"].append(str(currentBet)+","+str(currentBetNum))
                dataDict["P2 Payout"].append(payout)
                dataDict["P2 New Balance"].append(profile[1])
                print(Fore.BLUE)
                
    resultDataFrame = pd.DataFrame(dataDict,index = range(1,6))
    resultDataFrame.index.name = "Round"
    print(resultDataFrame)
    resultDataFrame.to_csv(scoreCardFile)
                
    scoreCardFile.close()  
            
if gameMode == "SIMULATION":
    
    simMode = input("MARTINGALE or NUMBERS").upper()
    if simMode == "MARTINGALE":
        scoreCardFile = open("martingale\\"+scoreCard,"w",newline="")
        dataDict = {
        "Bet Limit":[],
        "AI1 Balance":[],
        "AI1 Bet":[],
        "AI1 Payout":[],
        "AI1 New Balance":[],
        "AI2 Balance":[],
        "AI2 Bet":[],
        "AI2 Payout":[],
        "AI2 New Balance":[],
        "Email":[email]}

        martinBet = 500
        stayBet = 500
        players = [["AI 1(Martingale)",yourBalance,martinBet],["AI 2(Constant Bet)",houseBalance,stayBet]]
        
        for value in range(1000,1000000,2000):
            currentBetLimit = value
            dataDict["Bet Limit"].append(currentBetLimit)
            #The Martingale Trial: Increasing bet vs maintaining bet.
            for num in range(len(players)):
                oldBalance = players[num][1]
                print(players[num][:3])
                players[num][1] = spin(currentBetLimit,players[num][1],players[num][2],"BLACK")
                print("______________")
                payout = players[num][1]-oldBalance
                if players[num][0] == "AI 1(Martingale)":
                    if oldBalance>players[num][1]:
                        players[num][2]*=2
                    else:
                        players[num][2] = 500
                        
                    dataDict["AI1 Balance"].append(oldBalance)
                    dataDict["AI1 Bet"].append(players[num][2])
                    dataDict["AI1 Payout"].append(payout)
                    dataDict["AI1 New Balance"].append(players[num][1])
                else:
                    dataDict["AI2 Balance"].append(oldBalance)
                    dataDict["AI2 Bet"].append(players[num][2])
                    dataDict["AI2 Payout"].append(payout)
                    dataDict["AI2 New Balance"].append(players[num][1])
           
    
    elif simMode == "NUMBERS":
        scoreCardFile = open("numbers\\"+scoreCard,"w",newline="")
        dataDict = {
        "Bet Limit":[],
        "AI1 Balance":[],
        "AI1 Payout":[],
        "AI1 New Balance":[],
        "AI2 Balance":[],
        "AI2 Payout":[],
        "AI2 New Balance":[],
        "Email":[email]}
        #Betting on Numbers Vs. Colours Trial
        players = [["AI 1",yourBalance,500,"BLACK"],["AI 2",houseBalance,500,"36"]]
        for value in range(1000,1000000,2000):
            currentBetLimit = value
            dataDict["Bet Limit"].append(currentBetLimit)
            for num in range(len(players)):
                print(players[num][:3])
                oldBalance = players[num][1]
                players[num][1] = spin(currentBetLimit,players[num][1],players[num][2],players[num][3])
                print("______________")
                payout = players[num][1] - oldBalance
                if players[num][0] == "AI 1":
                    dataDict["AI1 Balance"].append(oldBalance)
                    dataDict["AI1 Payout"].append(payout)
                    dataDict["AI1 New Balance"].append(players[num][1])
                else:
                    dataDict["AI2 Balance"].append(oldBalance)
                    dataDict["AI2 Payout"].append(payout)
                    dataDict["AI2 New Balance"].append(players[num][1])
    resultDataFrame = pd.DataFrame(dataDict,index = range(1,501))
    resultDataFrame.index.name = "Round"
    resultDataFrame.to_csv(scoreCardFile)
            
    scoreCardFile.close()
exit()