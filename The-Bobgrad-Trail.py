# Import Modules
import numpy as np
import pygame as pg
import art
import time

# Initialize Variables
day = 0
progress = 0
occupation = ''
money = 0
multiplier = 0
wagon_name = ''
partner_name = ''
rations = 0
rations_cart = 0
medkits = 0
medkits_cart = 0
ammo = 0
ammo_cart = 0


# Define Functions
def init():
    """
    Initializes important game variables with user input
    :return: None
    """
    global occupation, money, multiplier, wagon_name, partner_name
    print()
    print("Who are you?")
    print("1. Banker (Most money, Fewest points)")
    print("2. Carpenter (Middle Ground")
    print("3. Farmer (Least money, Most points)")
    # Occupation
    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input("What is your choice?")
        if choice == '1':
            occupation = "banker"
            money = 150
            multiplier = 0.5
        elif choice == '2':
            occupation = "carpenter"
            money = 100
            multiplier = 1
        else:
            occupation = "farmer"
            money = 50
            multiplier = 2

    # Names
    correct = False
    while not correct:
        wagon_name = input("What is the name of the wagon leader?")
        partner_name = input("What is the name of their partner?")
        confirm = input("Are these names correct? (Y/Yes):")
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            correct = True


def shop():
    # TODO: Debug Shop
    """
    Presents the player with the shop menus
    :return: True when the function is no longer needed
    """
    global money, rations, rations_cart, medkits, medkits_cart, ammo, ammo_cart
    art.tprint("GENERAL STORE", "tarty1")
    print()
    print(f"Money you have: {money}   Total bill: {rations_cart * 5 + medkits_cart * 15 + ammo_cart}")
    print("1. Food")
    print("2. Ammo")
    print("3. Medical Kits")
    print("4. Finish & Pay")
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        choice = input("What is your choice?")
    if choice == '1':
        art.tprint("Food", "tarty2")
        print("Enough food to last you some time.")
        print("One ration costs $5.00")
        amount = ''
        while not amount.isnumeric():
            amount = input("How many would you like to buy? (0 to cancel)")
        amount = int(amount)
        if amount <= 0:
            return
        elif (amount * 5) > (money - (rations_cart + medkits_cart + ammo_cart)):
            print("Insufficient Funds!")
            time.sleep(1)
            return
        else:
            rations_cart += amount
            print(f"{amount} rations added!")
            time.sleep(1)
            return
    elif choice == '2':
        art.tprint("Ammo", "tarty2")
        print("You already own a rifle.")
        print("1 bullet is $1.00")
        amount = ''
        while not amount.isnumeric():
            amount = input("How many would you like to buy? (0 to cancel)")
        amount = int(amount)
        if amount <= 0:
            return
        elif amount > (money - (rations_cart + medkits_cart + ammo_cart)):
            print("Insufficient Funds!")
            time.sleep(1)
            return
        else:
            ammo_cart += amount
            print(f"{amount} bullets added!")
            time.sleep(1)
            return
    elif choice == '3':
        art.tprint("Medical Kits", "tarty2")
        print("Treats any ailment.")
        print("1 kit is $15.00")
        amount = ''
        while not amount.isnumeric():
            amount = input("How many would you like to buy? (0 to cancel)")
        amount = int(amount)
        if amount <= 0:
            return
        elif (amount * 15) > (money - (rations_cart + medkits_cart + ammo_cart)):
            print("Insufficient Funds!")
            time.sleep(1)
            return
        else:
            medkits_cart += amount
            print(f"{amount} kits added!")
            time.sleep(1)
            return
    else:
        art.tprint("Cost Breakdown", "tarty2")
        print(f"{rations_cart} rations: ${rations_cart * 5}.00")
        print(f"{ammo_cart} bullets: ${ammo_cart}.00")
        print(f"{medkits_cart} medical kits: ${medkits_cart * 15}.00")
        confirm = input("Is this correct? (Y/Yes):")
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            rations += rations_cart
            ammo += ammo_cart
            medkits += medkits_cart
            money -= (rations_cart * 5 + ammo_cart + medkits_cart * 15)
            rations_cart = 0
            ammo_cart = 0
            medkits_cart = 0
            print("Thank you for shopping!")
            time.sleep(1)
            return True
        else:
            rations_cart = 0
            ammo_cart = 0
            medkits_cart = 0
            return


def menu():
    """
    Shows the main menu for the game
    :return: True if this function does not need to be accessed anymore.
    """
    # Initial Menu
    art.tprint("THE BOBGRAD TRAIL", "tarty1")
    print("By Tommy, Graham, and Eric")
    print("--------------------------")
    print("You may...")
    print("1. Travel the trail")
    print("2. Learn about the trail")
    print("3. Exit")
    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input("What is your choice?")
    if choice == '1':
        init()
        return True
    elif choice == '2':
        print()
        print("The Bobgrad trail is a treacherous journey from East to West coast of an unknown region. "
              "What lies ahead is dangerous,but offers great reward.\n"
              "You can only claim your glory at the end of the trail if you can survive the journey there. "
              "Do you have what it takes?")
        print()
        input("Press Enter to Return")
    else:
        exit()


def progressbar(amt, maximum):
    """
    Displays a progress bar according to how close two values are
    :param amt: The amount to read as the "changing value"
    :param maximum: The maximum or '100%' value
    :return: None
    """
    ratio = amt / maximum
    num_bars = ratio // 0.05 + 1
    num_spaces = 20 - num_bars
    print("[" + ("#" * int(num_bars)) + (" " * int(num_spaces)) + "]")


def supplycheck():
    """
    Prints out a list of supplies the player currently has
    :return: None
    """
    print("--------------------------")
    art.tprint("SUPPLIES", "tarty2")
    print(f"Money: ${money}.00")
    print(f"Food: {rations} rations")
    print(f"Ammo: {ammo} bullets")
    print(f"Medical Supplies: {medkits} kits")
    print()
    input("Press Enter to Return")
    return

# Import Locals
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define Colors
black = (0, 0, 0)
white = (255, 255, 255)
gold = (252, 194, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initialize Pygame
pg.init()

# Set up Game Window
X = 1000
Y = 1000

# Setup
setup_complete = False
while not setup_complete:
    setup_complete = menu()

# Shop
print()
print("Before you leave, you best get fitted with supplies!\n"
      "Everything you'll need is available at the general store.")
print()
input("Press Enter to Continue")
shop_complete = False
while not shop_complete:
    shop_complete = shop()

print()
print("The day is young and your crew is ready. \n"
      "You set off on your journey.")
print()
input("Press Enter to continue")
#print(
#    "@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@***   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n         @@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@                    @@@@@@@@@@@@@@              (@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@                                                              ,@@@@@@@@\n@@@@@@                                                                    (@@@@@\n                                                                          (@@@@@\n                                                                             %@@\n@@@@@@@@@@@%        @@@@@@                                                   %@@\n@@@@@@@@@@@&////////((((((                                                   /((\n@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@                         ,@@@@@@@@                 %@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@@@@                 %@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@@@@              (@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@,                (@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@     .((((((((   (/(@@@@@@@@@@@,        (((     (@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@     ,@@@@@@@@      @@@@@@@@@@@,        @@@     (@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@        ,@@@@@@@@      @@@@@@@@@@@,     @@@@@@     (@@@@@\n@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@      @@@@@@@@(        @@@@@@     (@@@@@\n")

# Run Game
# TODO: This is mostly a concept, I am not sure how to code this efficiently
day1_complete = False
print("--------------------------")
art.tprint(f"DAY {day}", "tarty2")
print("9:00 AM     26°")
print("Lightly Cloudy")
print(f"PROGRESS: {progress * 100}%")
progressbar(progress, 1)
while not day1_complete:
    print()
    print("You set off on your journey")
    print("You may...")
    print("1. Continue")
    print("2. Check Map")
    print("3. Check Supplies")
    print("4. Check Crew")
    print("5. Use Supplies")
    print("6. Save & Exit")
    choice = input("What is your choice?")
running = True
# Main game loop
while running:
    exit()
    # Termination Check
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

# Terminate Program
pg.quit()
exit()

'''
screen = pg.display.set_mode((X,Y))
pg.display.set_caption('The Bobgrad Trail')
'''
'''
    # Background
    screen.fill(black)

    # Draw Text
    font = pg.font.Font('freesansbold.ttf', 64)
    text = font.render(input("Enter Text"), True, gold)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 8)

    # Update display
    screen.blit(text, textRect)
    pg.display.flip()
'''
