import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(3)


def intro(weapon, monster):
    print_pause("You find yourself inside ZOMBIELAND and\n"
                "you're standing ON ROAD, surrounded "
                "by wrecked car and buildings.\n")
    print_pause("As per our info " + monster + " is everywhere around "
                "here, in search of food.\n")
    print_pause("In front of you is a tower.\n")
    print_pause("To your left is gun shop.\n")
    print_pause("You have a shot gun (but not have much "
                "Bullets).\n")


def gunshop(weapon, monster):
    if "MACHINEGUN" in weapon:
        print_pause("\nYou enter into the gun shop.")
        print_pause("\nYou've been here before, and gotten all"
                    " the Bullets. It's just an empty space"
                    " now.")
        print_pause("\nYou walk back to the ROAD.\n")
    else:
        print_pause("\nYou enter into the gun shop.")
        print_pause("\nYou have found a MACHINEGUN")
        print_pause("\nNow you are carrying MACHINEGUN.")
        print_pause("\nYou walk back out to the ROAD.\n")
        weapon.append("MACHINEGUN")
    road(weapon, monster)


def tower(weapon, monster):
    print_pause("\nYou approach the main door of the tower.")
    print_pause("\nYou are about to enter when the door "
                "opens and out steps " + monster + ".")
    print_pause("\nGOD! This is " + monster + "'s tower!")
    print_pause("\nDeadly " + monster + " attacks you!\n")
    if "MACHINEGUN" not in weapon:
        print_pause("You feel a bit scared, "
                    "you are having low ammo.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "MACHINEGUN" in weapon:
                print_pause("\nAs the " + monster + " moves to attack, "
                            "you started fireing with MACHINEGUN.")
                print_pause("\nDeadly " + monster + " helpless "
                            "your new weapon seems to be killermachine!")
                print_pause("\nYou have rid the Earth from " + monster +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou did your best...")
                print_pause("but your gun is no match for the "
                            + monster + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back to the ROAD. "
                        "\nFortunately, you don't seem to have been "
                        "followed.\n")
            road(weapon, monster)
            break


def road(weapon, monster):
    print_pause("Enter 1 to enter the tower.")
    print_pause("Enter 2 to emter gun shop.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            tower(weapon, monster)
            break
        elif choice1 == "2":
            gunshop(weapon, monster)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nWait! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    weapon = []
    monster = random.choice(["DEADWOLF", "DEAD-BOSS", "DEAD-DRAGON"])
    intro(weapon, monster)
    road(weapon, monster)


play_game()
