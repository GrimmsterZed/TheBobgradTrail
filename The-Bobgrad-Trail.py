# Import Modules
import numpy as np
import pygame as pg
import art
import time
import random as ran
import math

# Initialize Pygame
pg.init()

# Define Colors
black = (0, 0, 0)
white = (255, 255, 255)
gold = (252, 194, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up Game Window
X = 1000
Y = 1000
screen = pg.display.set_mode((X, Y))
screen.fill(black)

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

bandit_chance = 0
pioneer_chance = 0
hunt_chance = 0

# TODO: Wagon Parts

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


def mapcheck():
    """
    Simulates checking map
    :return: None
    """
    print("--------------------------")
    art.tprint("MAP", "tarty2")
    print(f"PROGRESS: {progress}")
    print("You check your map, but how the hell are we gonna show that in the console?")
    print()
    input("Press Enter to Return")


def crewcheck():
    print("--------------------------")
    art.tprint("CREW", "tarty2")
    print(f"PROGRESS: {progress}")
    print("You check your crew. They aight.")
    print()
    input("Press Enter to Return")


def usesupplies():
    """
    Uses supplies
    :return: None
    """
    print("--------------------------")
    art.tprint("Supplies", "tarty2")
    print(f"PROGRESS: {progress}")
    print("You use supplies. (CODE ME)")
    print()
    input("Press Enter to Return")


def save():
    """
    Saves and exits the game
    :return: None
    """
    print("Saving...")
    #Do the saving
    print("Save successful!")
    input("Press Enter to exit.")
    exit()


def write(str,color, x,y):
    """
    :param str: what you want to be written unto the screen
    :param color: the color of the text in RGB
    :param x: x coordinate of the text
    :param y: y coordinate of the text
    """
    text = font.render(str, True, color,)
    screen.blit(text, (x,y))


def play(wav_file):
    """
    :param wav_file: .wav file you want to play
    """
    sound = mixer.Sound(wav_file)
    sound.play()


# Create Sprite Class
class Sprite:
    # function that initiates object in class with its parameters
    def __init__(self, image_file, X, Y):
        # holds the object's image
        self.image_file = pg.image.load(image_file)
        # holds the object's X coordinate
        self.X = X
        # holds the object's Y coordinate
        self.Y = Y
        # boolean for whether it is showing
        self.showing = True
        # boolean for whether it is moving
        self.moving = True

    # Object method that can be called with an object of this class
    def show(self):
        '''
        shows object on screen
        '''
        if self.showing:
            # takes image, and coordinates then draws it on the screen
            screen.blit(self.image_file, (self.X, self.Y))

    def moveX(self, speed):
        """
        moves object along x axis
        :param speed: speed at which the object is moving
        """
        if self.moving:
            self.X += speed

    def moveY(self, speed):
        """
        moves object along y axis
        :param speed: speed at which the object is moving
        """
        if self.moving:
            self.Y += speed

    def isTouching(self, other, range):
        '''
        see's whether two sprites are touching
        :param other: another sprite
        :param range: the distance they are to each other before they are considered touching
        :return: whether they are touching or not
        '''
        # formula for the distance between two vectors
        distance = math.sqrt((math.pow(self.X - other.X, 2)) + (math.pow(self.Y - other.Y,2)))
        if distance <= range:
            return True


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

# Day 0
day0_complete = False
print("--------------------------")
art.tprint(f"DAY {day}", "tarty2")
print("26°   Lightly Cloudy")
print(f"PROGRESS: {progress * 100}%")
progressbar(progress, 1)
while not day0_complete:
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
    while choice not in ['1', '2', '3', '4', '5', '6']:
        choice = input("What is your choice?")
    if choice == '1':
        day0_complete = True
    elif choice == '2':
        mapcheck()
    elif choice == '3':
        supplycheck()
    elif choice == '4':
        crewcheck()
    elif choice == '5':
        usesupplies()
    else:
        save()

# Run Game
running = True
# Main game loop
while running:
    day += 1
    # add progress
    # death check
    if progress == 50:
        print("50%")
    elif progress == 100:
        print("100%")
    else:
        print("--------------------------", flush=True)
        art.tprint(f"DAY {day}", "block")
        print("26°   Lightly Cloudy")
        print(f"PROGRESS: {progress * 100}%")
        progressbar(progress, 1)

        random = ran.randint(0,100)
        # TODO: Not garbage probability
        # Bandit
        if ran.randint(0,100) <= bandit_chance:
            print("Bandit Pass!")
            bandit_chance = 0
            pioneer_chance += 10
            hunt_chance += 20
        # Pioneer
        elif ran.randint(0,100) <= pioneer_chance:
            print("Pioneer Pass!")
            pioneer_chance = 0
            hunt_chance += 20
            bandit_chance += 5
        # Hunt
        elif ran.randint(0,100) <= hunt_chance:
            print("Hunt Pass!")
            hunt_chance = 0
            pioneer_chance += 10
            bandit_chance += 5
        else:
            hunt_chance += 20
            pioneer_chance += 10
            bandit_chance += 5
    input("Press Enter to continue")
    print('',flush=True)




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
