from random import random
from sys import exit

def uploadScore(userId, userScore):
    try:
        if userId == "end":
            scores=open("scores.txt","a")
            scores.write(str(userScore)+"\n")
        elif userId==False:
            pass
        else:
            scores=open("scores.txt")
            scores=scores.read()
            scores=scores.split("\n")
            outScore=open("scores.txt",'w')
            for x in range(len(scores)):
                if x==userId-1:
                    try:
                        scores[x]=userScore
                    except: pass
                outScore.write(str(scores[x])+'\n')
    except IOError:
        pass

def getUserScore(userId):
    try:
        scores=open("scores.txt")
        scores=scores.read()
        scores=scores.split("\n")
        counter=0
        for x in scores:
            counter+=1
            if counter ==userId:
                tmpScore=x
                break            
        if not tmpScore.isdigit(): tmpScore=0   #if it not a digit initialize tmpscore to zero
        else: tmpScore=int(tmpScore)
        return tmpScore 
    except IOError: 
        print("Error no scores.txt file")
        return 0

def getUser(username):
    try:
        usersFile=open("users.txt")
        OutUsersFile=open("users.txt",'a')
        users=usersFile.read()
        users=users.split("\n")
        counter=0
        for usr in users:
            counter+=1
            if username==usr:
                print('*******************WELCOME BACK {}!!!*******************'.format(username.upper()))
                return counter
        else:
            OutUsersFile.write(username + '\n')
            return "end" #return end to specify that user score should be placed at eof
    except IOError: 
        print("Error: no users.txt file in current directory")
        return False

def getAns():
    try:
        wordsFile=open("words.txt")
        wordsFile=wordsFile.read()
        words=wordsFile.split(" ")
        ansIndex=int((random()*100000)%len(words))
        answer=words[ansIndex]
        return answer
    except:
        print("words.txt have either been moved or deleted!!!\nPlace the game in the same folder as the words.txt file and try again!!!")
        print('*******************THANK YOU GOOD BYE*******************'.center(40))
        exit(0)

def lettersLeft(guessChar,currLettersLeft):
    newLettersSet=''
    for x in currLettersLeft:
        if x == guessChar:
            newLettersSet+='-'
        else: newLettersSet+=x
    return newLettersSet

def validateGuess(guessChar,currAns,answer):
    newCurrAns=''
    if (len(guessChar)!=1 or guessChar.isdigit()):
        print("INVALID INPUT!!!")
        return currAns
    elif guessChar in answer and guessChar not in currAns:
        print("CORRECT GUESS!!!")
        for x in range(len(answer)):
            if answer[x]==guessChar:
                newCurrAns+=answer[x]
            else: newCurrAns+=currAns[x]
        return newCurrAns
    else: 
        print("INCORRECT GUESS!!!")
        return currAns

def main():
    userScore=0
    username=input("Enter your username: ")
    username=username.upper()
    userId=getUser(username)
    if userId == False or userId == "end":
        print('*******************WELCOME NEW PLAYER: {}!!!*******************'.format(username.upper()))
    else: 
        userScore=getUserScore(userId)
    sep="--------------------------------------------------------------------------------"
    ask=1
    while ask != '0': 
        currLettersLeft='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
        answer=getAns()
        answer=answer.upper()
        ansLen=len(answer)
        currAns='-'*ansLen
        tmpCurrAns=currAns
        numOfTries=ansLen+1
        while numOfTries:
            print(sep)
            print("I am looking for a {} letter word: ".format(ansLen))
            print("Number of tries left: {}".format(numOfTries))
            guessChar=input("Enter a letter:      ")
            guessChar=guessChar.upper()
            currLettersLeft=lettersLeft(guessChar,currLettersLeft)
            currAns=validateGuess(guessChar,currAns,answer)
            if currAns==tmpCurrAns:
                print("Letter not in word!!!\nCurrent status : {}".format(currAns))
                numOfTries-=1
            else:
                print("Bravo!!!; Current status: {} ".format(currAns))
                tmpCurrAns=currAns
                if currAns==answer:
                    userScore+=1
                    print(sep)
                    print("*****************CONGRATULATIONS!!!*****************".center(len(sep)))
                    print("*********{} your overal score is: {}*********".format(username,userScore).center(len(sep)))
                    print(sep)
                    break;
            print(currLettersLeft)
            print(sep)
        print("Answer = {}; value = {}".format(answer,currAns))
        print(sep)
        ask=input("press (0) to exit or any key to continue: ")
        print(sep)
        print("\n\n")
    uploadScore(userId, userScore)
    exit(0)

if __name__ == "__main__": main()
