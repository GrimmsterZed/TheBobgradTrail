import pygame as pg
screen = pg.display.set_mode((800,600))

# so yeah, these are too big but I was too lazy to find other sprites. We can change it later
bImg = pg.image.load("Images/Title/letter-b.png")
oImg = pg.image.load("Images/Title/o.png")
bImg2 = pg.image.load("Images/Title/letter-b.png")
gImg = pg.image.load("Images/Title/search.png")
rImg = pg.image.load("Images/Title/r.png")
aImg = pg.image.load("Images/Title/a.png")
dImg = pg.image.load("Images/Title/d.png")
tImg = pg.image.load("Images/Title/t.png")
rImg2 = pg.image.load("Images/Title/r.png")
aImg2 = pg.image.load("Images/Title/a.png")
iImg = pg.image.load("Images/Title/r.png")
lImg = pg.image.load("Images/Title/l.png")

def title(x,y, spacing):
    '''
    :param x: x coordinate of first letter
    :param y: y coordinate of first letter
    :param spacing: space between letters
    '''
    # draws the image unto the screen
    screen.blit(bImg, (x,y))
    screen.blit(oImg, (x + spacing, y + spacing))
    screen.blit(bImg2, (x + spacing*2, y + spacing*2))
    screen.blit(gImg, (x + spacing*3, y + spacing*3))
    screen.blit(rImg, (x + spacing*4, y + spacing*4))
    screen.blit(aImg, (x + spacing*5, y + spacing*5))
    screen.blit(dImg, (x + spacing*6, y + spacing*6))
    screen.blit(tImg, (x + spacing*8, y + spacing*8))
    screen.blit(rImg2, (x + spacing*9, y + spacing*9))
    screen.blit(aImg, (x + spacing*10, y + spacing*10))
    screen.blit(iImg, (x + spacing*11, y + spacing*11))
    screen.blit(lImg, (x + spacing*12, y + spacing*12))



