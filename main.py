from art import logo
print(logo)
import random

def generazione(mano_str, mano_int):


def pescaancora(mano_str,mano_int):
    tu = ""
    while True:
        print("Wanna take card?")
        choice = scelta()
        if choice:
            tu += str(random.choice(cards))
            mano_str += " " + tu
            mano_int += int(tu)
        elif choice == False:
            print(f"Your hand {mano_str} ")
            return mano_int
        print(f"Your hand:{mano_str} ={mano_int}")
        if mano_int <= 21:
            if mano_int == 21:
                print(f"BlackJack{mano_str} = {mano_int}")
                return mano_int
            print(f"Your hand {mano_str} = {mano_int}")
            continue
        else:
            check = mano_str.find("11")
            if check != -1:
                mano_str = mano_str[:check] + mano_str[check + 1:]
                mano_int = mano_int - 10
                print(mano_str, mano_int)
                input("stop")
            else:
                print(f"You lose {mano_str} = {mano_int}")
                return mano_int




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
    mano_ai_str = ""
    mano_ai_int = 0
    mano_str = ""
    mano_int = 0
    for x in range(2):
        ia = str(random.choice(cards))
        mano_ai_int += int(ia)
        mano_ai_str += " " + ia
    print(f"{mano_ai_int} {mano_ai_str} mano ia")
    for y in range(2):
        tu = str(random.choice(cards))
        mano_str += " " + tu
        mano_int += int(tu)
    print(f"Your hand:{mano_str} = {mano_int}")
    mano = pescaancora(mano_str,mano_int)
    if mano == 'y':
        print("you lost")
        return



if __name__ == '__main__':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    main()