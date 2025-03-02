def menu():
    print("**Dhaweeye**")
    print("Dooro mid kamida adeegyadan:-")
    print("1- Dhaweeye")
    print("2- Dhaweeye+")
    print("3- Mooto")
    print("4- Somgas")
    print("5- Kalaabo Dalabka")


def dhaweeye():
    print("**Dhaweeye**")
    print("Ma hubtaa inaad dalbato adeega dhaweeye")
    print("1- Haa")
    print("2- Maya")
    dalab = int(input("Dooro (1-2): "))
    if dalab == 1:
        print("**Dhaweeye**")
        print("Waxad dalbatay Adeega Dhaweeye")
    elif dalab == 2:
        print("**Dhaweeye**")
        print("Waad ka laabatay Adeega Dhaweeye. Mahadsanid.")
    else:
        print("Dalab sax ah maadan galinin Fadlan isku day markale!")


def dhaweeyeplus():
    print("**Dhaweeye**")
    print("Ma hubtaa inaad dalbato adeega dhaweeye+")
    print("1- Haa")
    print("2- Maya")
    dalab = int(input("Dooro (1-2): "))
    if dalab == 1:
        print("**Dhaweeye**")
        print("Waxad dalbatay Adeega Dhaweeye+")
    elif dalab == 2:
        print("**Dhaweeye**")
        print("Waad ka laabatay Adeega Dhaweeye. Mahadsanid.")
    else:
        print("Dalab sax ah maadan galinin Fadlan isku day markale!")


def mooto():
    print("**Dhaweeye**")
    print("Ma hubtaa inaad dalbato adeega Mooto")
    print("1- Haa")
    print("2- Maya")
    dalab = int(input("Dooro (1-2): "))
    if dalab == 1:
        print("**Dhaweeye**")
        print("Waxad dalbatay Adeega Mooto")
    elif dalab == 2:
        print("**Dhaweeye**")
        print("Waad ka laabatay Adeega Dhaweeye. Mahadsanid.")
    else:
        print("Dalab sax ah maadan galinin Fadlan isku day markale!")


def somgas():
    print("**Dhaweeye**")
    print("Ma hubtaa inaad dalbato adeega Somgas")
    print("1- Haa")
    print("2- Maya")
    dalab = int(input("Dooro (1-2): "))
    if dalab == 1:
        print("**Dhaweeye**")
        print("Waxad dalbatay Adeega Somgas")
    elif dalab == 2:
        print("**Dhaweeye**")
        print("Waad ka laabatay Adeega Dhaweeye. Mahadsanid.")
    else:
        print("Dalab sax ah maadan galinin Fadlan isku day markale!")


def main():
    while True:
        menu()
        choice = int(input("Kadooro kuwa sare (1-5): "))
        if choice == 1:
            dhaweeye()
        elif choice == 2:
            dhaweeyeplus()
        elif choice == 3:
            mooto()
        elif choice == 4:
            somgas()
        elif choice == 5:
            print("Waad ka laabatay Adeega Mahadsanid!")
            break

        else:
            print("Dalab sax ah maadan galinin Fadlan isku day markale!")

if __name__ == '__main__':
    main()


