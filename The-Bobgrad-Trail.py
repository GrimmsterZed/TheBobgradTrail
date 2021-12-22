# Import Modules
import numpy as np
import pygame as pg

# Initialize Variables
occupation = ''
money = 0
multiplier = 0
wagon_name = ''
partner_name = ''
rations = 0
medkits = 0
ammo = 0

# Define Functions
def init():
    '''
    Initializes important game variables with user input
    :return: None
    '''
    global occupation, money, multiplier, wagon_name, partner_name
    print()
    print("Who are you?")
    print("1. Banker (Most money, Fewest points)")
    print("2. Carpenter (Middle Ground")
    print("3. Farmer (Least money, Most points)")
    # Occupation
    menuchoice = ''
    while menuchoice not in ['1', '2', '3']:
        menuchoice = input("What is your choice?")
        if menuchoice == '1':
            occupation = "banker"
            money = 150
            multiplier = 0.5
        elif menuchoice == '2':
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
        confirm = input("Are these names correct? (Y/N):")
        if confirm.lower() == 'y':
            correct = True

def shop():
    '''
    Presents the player with the shop menus
    :return: None
    '''
    global money, rations, medkits, ammo
    print()
    print("Before you leave, you best get fitted with supplies!\n"
          "Everything you'll need is available at the general store.")

def menu():
    '''
    Shows the main menu for the game
    :return: True if this function does not need to be accessed anymore.
    '''
    # Initial Menu
    print("--------------------------")
    print("THE BOBGRAD TRAIL")
    print("By Tommy, Graham, and Eric")
    print("--------------------------")
    print("You may...")
    print("1. Travel the trail")
    print("2. Learn about the trail")
    print("3. Exit")
    menuchoice = ''
    while menuchoice not in ['1', '2', '3']:
        menuchoice = input("What is your choice?")
        if menuchoice == '1':
            init()
            return True
        elif menuchoice == '2':
            print()
            print("The Bobgrad trail is a treacherous journey from East to West coast of an unknown region. What lies ahead is dangerous, "
                  "but offers great reward.\nYou can only claim your glory at the end of the trail if you can survive the journey there. Do you have what it takes?")
            print()
            input("Press Enter to Return")
        else:
            exit()


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
shop_complete = False
while not shop_complete:
    shop_complete = shop()

# Run Game
running = True
# Main game loop
while running:

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