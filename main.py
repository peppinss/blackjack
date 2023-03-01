from art import logo
print(logo)
import time
import random

def money1():
    while True:
        try:
            money = int(input("Sit with how many chips?: "))
            if money > 0:
                return money
        except:
            print("It must be a value > 0")

def betting():
    while True:
        try:
            bet = int(input("how mutch u wanna bet: "))
            if bet > 0 and bet <= money:
                return bet
            elif bet < 0:
                print("Your bet must be at least 1 dollar")
            else:
                print(f"You don't have enough money, your balance is {money}")
        except:
            print("i did not understand could you please type it again?")

def generazione(mano_str, mano_int, utente):
    if mano_int == 21:
        print(f"{utente}: scored blackjack {mano_str}")
        time.sleep(1)
        return mano_int
    choice = False
    while True:
        if utente == "banco" and mano_int >= 17:
            return mano_int
        elif not utente == "banco":
            print("Wanna take card?")
            choice = scelta()
        if choice or utente == "banco":
            tu = ""
            tu += str(random.choice(cards))
            print(f"The card is {tu}")
            time.sleep(1)
            mano_str += " " + tu
            mano_int += int(tu)

        elif not choice and not utente == "banco":
            print(f"Your hand {mano_str} = {mano_int} ")
            return mano_int
        print(f"{utente} hand:{mano_str} ={mano_int}")
        if mano_int <= 21:
            if mano_int == 21:
                print(f"{utente} does BlackJack{mano_str} = {mano_int}")
                return 21
            continue
        else:
            check = mano_str.find("11")
            if check >= 0:
                mano_str = mano_str[:check] + " " + mano_str[(check + 1):]
                mano_int = mano_int - 10
                print("ace has ben converted to 1")
                print(f"{mano_str} = {mano_int}")
            else:
                print(f"{utente} exceeded 21: {mano_str} = {mano_int}")
                return False

def scelta():
    while True:
        choice = input().lower()
        if choice == "y" or choice == "yes":
            return True
        elif choice == "n" or choice == "no":
            return False
        else:
            print("i did not understand could you please type it again?")


def main():
    y = 0
    mano_ai_str,mano_str = "",""
    mano_ai_int,mano_int = 0,0
    for x in range(2):
        ia = str(random.choice(cards))
        if x == 0:
            onecard = ia
        if ia == "11":
            y += 1
        if y == 2:
            print("You got double ace, one of them as been changed to 1")
            ia = "1"
        mano_ai_int += int(ia)
        mano_ai_str += " " + ia
    print(f"Dealer: {onecard} * ")
    for z in range(2):
        tu = str(random.choice(cards))
        if tu == "11":
            y += 1
        if y == 2:
            print("You got double ace, one of them as been changed to 1")
            tu = "1"
        mano_str += " " + tu
        mano_int += int(tu)
    print(f"Your hand:{mano_str} = {mano_int}")
    mano = generazione(mano_str,mano_int,utente1)
    if not mano:
        return(money - bet)

    manoia = generazione(mano_ai_str,mano_ai_int,utente="banco")
    if not manoia:
        return(money + bet)
    time.sleep(3)
    if mano > manoia or manoia == False:
        print(f"You won, final resoults {utente1}= {mano} banco= {manoia} ")
        return (money + bet)
    elif manoia > mano or mano == False:
        print(f"you lost, final resoults {utente1}= {mano} banco= {manoia}")
        return (money - bet)
    else:
        print(f"draw, final resoults {utente1}= {mano} banco= {manoia}")
        return money

if __name__ == '__main__':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    money = money1()
    utente1 = input("Insert your username: ")
    print(f"You join the table with {money}$")
    while True:
        bet = betting()
        money = main()
        time.sleep(1)
        print(f"your balance is now {money}")
        if money == 0:
            print("I'm sorry but you don't have enough money to play,")
            break
        print("play again?")
        again = scelta()
        if not again:
            print(f"Thanks for playing, you ended up with {money}")
            break