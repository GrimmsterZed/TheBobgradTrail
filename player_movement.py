import pygame as pg


def move_playerX(event,speed, playerX):

    # Set Boundaries
    """if playerX - speed <= 0:
        return (0,0)
    elif playerX + speed >= 770:
        return (0,0)
    if playerY - speed <= 0:
        return (0,0)
    elif playerY + speed >= 580:
        return (0,0)
"""

    playerX_change = 0
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_a:
            #print("Should move to the left")
            playerX_change = -speed
        if event.key == pg.K_RIGHT or event.key == pg.K_d:
            #print("Should move to the right")
            playerX_change = speed

    # stops movement after key is let go
    if event.type == pg.KEYUP and not event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_a or event.key == pg.K_d:
            playerX_change = 0
    return playerX_change

def move_playerY(event,speed, playerY):
    playerY_change = 0
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_DOWN or event.key == pg.K_s:
            #print("Should move down")
            playerY_change = speed
        if event.key == pg.K_UP or event.key == pg.K_w:
            #print("Should move up")
            playerY_change = -speed

    # stops movement after key is let go
    if event.type == pg.KEYUP and not event.type == pg.KEYDOWN:
        if event.key == pg.K_UP or event.key == pg.K_DOWN or event.key == pg.K_w or event.key == pg.K_s:
            playerY_change = 0

    return playerY_change