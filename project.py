import random
def cost():
    money = 1000
    bet = int(input("How much of your 1000 dollars do you want to bet(whole number)? "))
    if bet> money:
        print("You don't have the funds for that kind of bet")
    elif bet < 0:
        print("You can't bet negative values")
    new_money = money - bet
    return bet

def gamble ():
    randList = []
    for i in range(10):
        randList.append(random.randint(1,100))
    num = 0
    attemps = 5
    new_bet = cost() * 2
    # uncomment the print statment for testing
    #print(randList)
    while num not in randList:
        
        num = int(input("Pick a whole number between 1 and 100 "))
        if num not in randList:
            attemps -= 1
            print("WRONG Try again")
            print(f'You have ' + str(attemps) + " attemps left")
        if num <=0 or num>=100:
            print("Not in the range you have wasted a guess")
    
        if num in randList:
            print("Great job you win!")
            print(f'You won $'+ str(new_bet))
            break 
        elif attemps == 0:
            print("You have failed")
            print(f'You lost your entire bet')
            break

def main():
    gamble()

main()
        


