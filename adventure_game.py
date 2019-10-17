import time
import random


def print_pause(string):
    print(string)
    time.sleep(1)


def intro(weapon, health, boss):
    print_pause("You wake up in an illuminated cavern.")
    print_pause("All you have with you are the clothes you are wearing.")
    print_pause("Your stomach grumbles. You're quite hungry. <Your HP 10/100>")
    cavern(weapon, health, boss)


def cavern(weapon, health, boss):
    print_pause("You need to get home before nighttime, "
                "so you can't stick around here for long.")
    print_pause("You see light coming from some fluorescent "
                "mushrooms growing around you.")
    while True:
        cav_choice = input("Enter 1 to exit the cave.\n"
                           "Enter 2 to collect mushrooms to eat.\n")
        if cav_choice == '1':
            field(weapon, health, boss)
            break
        elif cav_choice == '2':
            if health == 100:
                print_pause("You don't really need to eat anymore.")
            else:
                health = 100
                print_pause("Surprisingly, these mushrooms are enchanted!\n"
                            "You feel completely refreshed and invigorated! "
                            "<Your HP 100/100>")
                cavern(weapon, health, boss)
                break
        else:
            print_pause("(Please enter 1 or 2.)")


def field(weapon, health, boss):
    print_pause("You find yourself in an open field inside the Western Forest,"
                "\nand your home is in Central Village to the east.")
    print_pause("You see a large road heading east, "
                "certainly the route back home.")
    print_pause("You see an off-beaten path to the side "
                "leading into shrubs and branches.")
    while True:
        field_choice = input("Enter 1 to head down the major road east.\n"
                             "Enter 2 to go down the side route.\n"
                             "Enter 3 to go back into the cavern.\n")
        if field_choice == '1':
            boss_encounter(weapon, health, boss)
            break
        elif field_choice == '2':
            find_weapon(weapon, health, boss)
            break
        elif field_choice == '3':
            cavern(weapon, health, boss)
            break
        else:
            print_pause("(Please enter 1, 2, or 3.)")


def find_weapon(weapon, health, boss):
    print_pause("Pushing aside branches and stepping through the brush,\n"
                "you find a small open area in front of an unscalable wall.")
    if "wooden bow and arrow" and "copper sword" and "quartz amulet" in weapon:
        print_pause("There's nothing here.")
    else:
        print_pause("You see something glinting in the very back.")
        weapons = ["wooden bow and arrow", "copper sword", "quartz amulet"]
        weapon = random.choice(weapons)
        print_pause(f"It's a {weapon}! You feel much stronger "
                    "with this compared to your bare hands.")
    print_pause("You turn around and head back into the field.")
    field(weapon, health, boss)


def boss_encounter(weapon, health, boss):
    if boss == "":
        bosses = ["cyclops", "goblin", "witch"]
        boss = random.choice(bosses)
        print_pause(f"As you go down the road, suddenly a {boss}"
                    " jumps out of nowhere and blocks your path!")
    print_pause(f"The {boss} seems ready to fight and won't let you pass. "
                "It looks pretty strong.")
    while True:
        boss_choice = input("Enter 1 to fight the boss.\n"
                            "Enter 2 to run away.\n")
        if boss_choice == '1':
            fight(weapon, health, boss)
            break
        elif boss_choice == '2':
            field(weapon, health, boss)
            break
        else:
            print_pause("(Please enter 1 or 2.)")


def fight(weapon, health, boss):
    boss_health = 100
    print_pause("The boss is at full health now.")
    while health > 0 and boss_health > 0:
        print_pause(f"You attack the {boss}!")
        if (weapon == "wooden bow and arrow" or
                weapon == "copper sword" or
                weapon == "quartz amulet"):
            damage = random.randint(20, 40)
            boss_health -= damage
            print_pause(f"Your {weapon} is super effective!")
            print_pause("You did "+str(damage)+" damage to the boss!")
            if boss_health >= 0:
                print_pause(f"<Boss HP {boss_health}/100>")
            else:
                print_pause("<Boss HP 0/100>")
        else:
            damage = random.randint(5, 15)
            boss_health -= damage
            print_pause("You punch the boss with your bare hands!")
            print_pause("You did "+str(damage)+" damage to the boss!")
            if boss_health >= 0:
                print_pause(f"<Boss HP {boss_health}/100>")
            else:
                print_pause("<Boss HP 0/100>")
        if boss_health > 0:
            print_pause(f"The {boss} attacks back!")
            damage = random.randint(10, 25)
            health -= damage
            print_pause("You take " + str(damage) + " damage!")
            if health >= 0:
                print_pause(f"<Your HP {health}/100>")
            else:
                print_pause("<Your HP 0/100>")
        if health <= 0:
            print_pause("You have died.")
            print_pause("GAME OVER.")
            break
        elif boss_health <= 0:
            print_pause(f"You've slayed the {boss}!")
            print_pause("You make it back home safely to your loving "
                        "family and live happily ever after!")
            break
        while True:
            cont = input("Do you want to (1) keep fighting or (2) run away?\n")
            if cont == '2':
                field(weapon, health, boss)
                break
            elif cont == '1':
                break
            else:
                print_pause("(Please input 1 or 2.)")
    while True:
        again = input("Would you like to play again? (Yes/No)\n").lower()
        if again == 'yes':
            start_game()
            break
        elif again == 'no':
            print_pause("Thank you for playing!\n")
            break
        else:
            print_pause("Sorry, I don't understand that.")


def start_game():
    weapon = ""
    health = 10
    boss = ""
    intro(weapon, health, boss)


start_game()
