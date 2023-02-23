import matplotlib.pyplot as plt
import pandas as pd
import os

analysisMode=input("Mode:ANALYSE/PREDICT").upper()
gameMode = input("Results to be predicted: singleplayer/multiplayer/martingale/numbers").lower()

email = ""
validEmail = False
while not validEmail:
    email = input("Enter your valid email to access your game data:")
    if email.count("@")==1 and email.count(".")>0:
        validEmail = True


if analysisMode == "ANALYSE":

    scoreCard = input("Name of scorecard file(including file type suffix):")
    resultDataFrame = pd.read_csv(gameMode+"\\"+scoreCard)
    if resultDataFrame.loc[0]["Email"] != email:
        print("You do not have access to this file!")
        exit()
    header = list(resultDataFrame.columns)
    if header[2] == "Balance":
        #singleplayer
        resultDataFrame.plot(x="Round",y="New Balance")
        resultDataFrame.plot(x="Round",y="Payout")
        plt.show()
        balances = list(resultDataFrame["New Balance"])
        payouts = list(resultDataFrame["Payout"])
        meanBalance = sum(balances)/len(balances)
        meanPayout = sum(payouts)/len(payouts)
        balances = sorted(balances)
        inQuLowerIndex = len(balances)*0.25
        if inQuLowerIndex // 1 != 0:
            inQuLower = (balances[int(inQuLowerIndex)]+balances[int(inQuLowerIndex)+1])/2
        inQuUpperIndex = len(balances)*0.75
        if inQuUpperIndex // 1 != 0:
            inQuUpper = (balances[int(inQuUpperIndex)]+balances[int(inQuUpperIndex)+1])/2
        inQuRange = [inQuLower,inQuUpper]
        
        
        print("Mean Balance:",meanBalance)
        print("Mean Payout:",meanPayout)
        print("Interquartile Range:",inQuRange)
    elif header[2] == "P1 Balance":
        #multiplayer
        fig1,ax1 = plt.subplots()
        resultDataFrame.plot(x="Round",y="P1 New Balance",ax = ax1)
        resultDataFrame.plot(x="Round",y="P2 New Balance",ax = ax1)
        plt.show()
        for num in (1,2):
            balances = list(resultDataFrame["P"+str(num)+" New Balance"])
            payouts = list(resultDataFrame["P"+str(num)+" Payout"])
            meanBalance = sum(balances)/len(balances)
            meanPayout = sum(payouts)/len(payouts)
            balances = sorted(balances)
            inQuLowerIndex = len(balances)*0.25
            if inQuLowerIndex // 1 != 0:
                inQuLower = (balances[int(inQuLowerIndex)]+balances[int(inQuLowerIndex)+1])/2
            inQuUpperIndex = len(balances)*0.75
            if inQuUpperIndex // 1 != 0:
                inQuUpper = (balances[int(inQuUpperIndex)]+balances[int(inQuUpperIndex)+1])/2
            inQuRange = [inQuLower,inQuUpper]
            print("Player "+str(num)+":")
            print("Mean Balance:",meanBalance)
            print("Mean Payout:",meanPayout)
            print("Interquartile Range:",inQuRange)
    elif header[3] == "AI1 Bet":
        #martingale
        for num in (1,2):
            balances = list(resultDataFrame["AI"+str(num)+" New Balance"])
            payouts = list(resultDataFrame["AI"+str(num)+" Payout"])
            meanBalance = sum(balances)/len(balances)
            meanPayout = sum(payouts)/len(payouts)
            balances = sorted(balances)
            inQuLowerIndex = len(balances)*0.25
            if inQuLowerIndex // 1 != 0:
                inQuLower = (balances[int(inQuLowerIndex)]+balances[int(inQuLowerIndex)+1])/2
            inQuUpperIndex = len(balances)*0.75
            if inQuUpperIndex // 1 != 0:
                inQuUpper = (balances[int(inQuUpperIndex)]+balances[int(inQuUpperIndex)+1])/2
            inQuRange = [inQuLower,inQuUpper]
            print("AI"+str(num)+":")
            print("Mean Balance:",meanBalance)
            print("Mean Payout:",meanPayout)
            print("Interquartile Range:",inQuRange)
        
        fig1,(ax1,ax2)= plt.subplots(2,1,figsize = (8,7))
        resultDataFrame.plot(x="Round",y="AI1 New Balance",ax = ax1)
        resultDataFrame.plot(x="Round",y="AI2 New Balance",ax = ax1)
        resultDataFrame.plot(x="Round",y = "Bet Limit",ax = ax1)
        resultDataFrame.plot(x="Round",y="AI2 Payout",ax = ax1)
        resultDataFrame.plot(x="Round",y="AI2 Payout",ax = ax1)
        resultDataFrame.plot(x="Round",y="AI1 Bet",ax = ax1)
        resultDataFrame.plot.box(y=["AI1 New Balance","AI2 New Balance"],ax = ax2)
        plt.show()
        
        
    elif header[3] == "AI1 Payout":
        #numbers
        #Note: AI2 is the numbers strategy
        
        for num in (1,2):
            balances = list(resultDataFrame["AI"+str(num)+" New Balance"])
            payouts = list(resultDataFrame["AI"+str(num)+" Payout"])
            meanBalance = sum(balances)/len(balances)
            meanPayout = sum(payouts)/len(payouts)
            balances = sorted(balances)
            inQuLowerIndex = len(balances)*0.25
            if inQuLowerIndex // 1 != 0:
                inQuLower = (balances[int(inQuLowerIndex)]+balances[int(inQuLowerIndex)+1])/2
            inQuUpperIndex = len(balances)*0.75
            if inQuUpperIndex // 1 != 0:
                inQuUpper = (balances[int(inQuUpperIndex)]+balances[int(inQuUpperIndex)+1])/2
            inQuRange = [inQuLower,inQuUpper]
            print("AI"+str(num)+":")
            print("Mean Balance:",meanBalance)
            print("Mean Payout:",meanPayout)
            print("Interquartile Range:",inQuRange)
        
        fig1,(ax1,ax2)=plt.subplots(2,1,figsize =(8,7))
        resultDataFrame.plot(x="Round",y="AI1 New Balance",ax = ax1)
        resultDataFrame.plot(x="Round",y="AI2 New Balance",ax = ax1)
        resultDataFrame.plot(kind = "box",y=["AI1 New Balance","AI2 New Balance"],ax = ax2)
        plt.show()
        
elif analysisMode == "PREDICT":
    fileList=list(os.walk(gameMode))[0][2]
    if len(fileList)==0:
        print("Play Roulette to generate more game data to analyse for predictions.")
        exit()
    if gameMode == "singleplayer":
        singleWinningsList = []
        singleWins = 0
        singleLosses = 0
        for myDir in fileList:
            resultDataFrame = pd.read_csv(gameMode+"\\"+myDir)
            if resultDataFrame.loc[0]["Email"] == email:
                winnings = (resultDataFrame.loc[4]["New Balance"])
                if winnings > 0:
                    singleWins+=1
                elif winnings<0:
                    singleLosses+=1
                singleWinningsList.append(winnings)
        try :
            winLossRatio = (singleWins/singleLosses)
        except ZeroDivisionError:
            winLossRatio = 1
        print("You have won",singleWins,"games and lost",singleLosses,"games. Your win/loss ratio is ",round(winLossRatio,3),"across",len(singleWinningsList),"games.")
        print("You have an estimated",str(round(100*(singleWins/len(singleWinningsList)),3))+"%","chance of winning your next game using your current strategy based on this data.")
        print("Your total winnings across all games come out to",sum(singleWinningsList),"with an average profit per game of",round(sum(singleWinningsList)/len(singleWinningsList),2),".")
    elif gameMode == "multiplayer":
        p1WinningsList = []
        p2WinningsList = []
        p1Wins = 0
        p2Wins = 0
        for myDir in fileList:
            resultDataFrame = pd.read_csv(gameMode+"\\"+myDir)
            if resultDataFrame.loc[0]["Email"] == email:
                p1Winnings = resultDataFrame.loc[4]["P1 New Balance"]
                p1WinningsList.append(p1Winnings)
                p2Winnings = resultDataFrame.loc[4]["P2 New Balance"]
                p2WinningsList.append(p2Winnings)
                
                p1Wins += int(p1Winnings>p2Winnings)
                p2Wins += int(p1Winnings<p2Winnings)
                
        print("Player 1: You have won",p1Wins,"games and lost",p2Wins,"games out of",len(p1WinningsList),"games.")
        print("Your chance of winnings against Player 2 if both of you continue with your current strategies is",str(round(100*(p1Wins/len(p1WinningsList)),3))+"%.")
        print("Your total winnings across all games come out to",sum(p1WinningsList),"with an average profit per game of",round(sum(p1WinningsList)/len(p1WinningsList),2),".")
        print("-----------------------------------------------------")
        print("Player 2: You have won",p2Wins,"games and lost",p1Wins,"games out of",len(p2WinningsList),"games.")
        print("Your chance of winnings against Player 2 if both of you continue with your current strategies is",str(round(100*(p2Wins/len(p2WinningsList)),3))+"%.")            
        print("Your total winnings across all games come out to",sum(p2WinningsList),"with an average profit per game of",round(sum(p2WinningsList)/len(p2WinningsList),2),".")
        
    elif gameMode == "martingale" or gameMode == "numbers":
        simWinningsList = []
        stayWinningsList = []
        simWins = 0
        stayWins = 0
        
        for myDir in fileList:
            resultDataFrame = pd.read_csv(gameMode+"\\"+myDir)
            #while an extended data set is taken for predicting strategy effectiveness in analysis,
            #for prediction the first 5 rounds are used as an accurate representation of a real game
            if gameMode == "martingale":
                simWinnings = resultDataFrame.loc[4]["AI1 New Balance"]
                stayWinnings = resultDataFrame.loc[4]["AI2 New Balance"]
            else:
                simWinnings = resultDataFrame.loc[4]["AI2 New Balance"]
                stayWinnings = resultDataFrame.loc[4]["AI1 New Balance"] 
            simWins += int(simWinnings>stayWinnings)
            stayWins += int(simWinnings<stayWinnings)
            simWinningsList.append(simWinnings)
            stayWinningsList.append(stayWinnings)
            
        simWinRate = str(round(100*(simWins/len(simWinningsList)),3))
        gameMode = gameMode[0].upper() + gameMode[1:]
        print("The ",gameMode," Strategy has a win rate of",str(round(100*(simWins/len(simWinningsList)),3)),"% against a constant bet of 500 on even odds after",len(simWinningsList),"games.")
        print("Based on current data the ",gameMode," strategies gives an mean profit of",round(sum(simWinningsList)/len(simWinningsList),2),"in comparison to the constant bet strategy's mean profit of",round(sum(stayWinningsList)/len(stayWinningsList),2),".")
            
            
