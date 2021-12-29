import pygame as pg
from pygame import mixer # for sound
import math # for detection of other sprites
import title_animation as tit

# for title animation
titleX = -800


pg.init()

# creating a class that can hold objects. The class is for any asset that wants to be on screen.
class Sprite:
    # function that initiates object in class with it's parameters
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

# setting up font of text
font = pg.font.Font('freesansbold.ttf', 30)

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


# creating an object of class 'Sprite'
mascot = Sprite("Images/bobgrad_icon.png", 400, 300)


#Setting up screen
screen = pg.display.set_mode((800,600))

# Window title and icon
pg.display.set_caption("Bobgrad Trail")
icon = pg.image.load("Images/bobgrad_icon.png")
pg.display.set_icon(icon)

# background
#background = pygame.image.load()


# background music
#mixer.music.load()
#mixer.music.play(-1) # to loop


# Import Locals
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

running = True
while running:
    screen.fill((69, 69, 69))

    # Termination Check
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False


    # function for the title
    tit.title(titleX, 20, 50)
    if titleX <= 20:
        titleX += 3

    # Testing class methods
    mascot.show()
    mascot.moveY(2)
    if mascot.Y >= 450:
        mascot.showing = False



    # testing writing
    write("Hello world", (255,255,255), 20, 20)

    pg.display.update()
