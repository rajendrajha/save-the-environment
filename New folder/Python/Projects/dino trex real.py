import pygame
pygame.init()
x=0
y=200
d= 0
i=0
game= pygame.display.set_mode((1000,400))
pygame.display.set_caption("Dino-Trex")
dinosaur= pygame.image.load('dino,.jpg')
sin= pygame.transform.scale(dinosaur,(100,100))
dino= pygame.image.load('stag.png')
trex= pygame.transform.scale(dino,(1000,400))
Cloud= pygame.image.load('cloud.png')
Cloud_SIZE= pygame.transform.scale(Cloud,(150,50))
exit= False
font= pygame.font.SysFont(None,55)
def main(text,color,x,y):
   dt= font.render(text,True,color)
   game.blit(dt,[x,y])
def menu():
    a= pygame.image.load('screen.jpg')
    ai= pygame.transform.scale(a,(1000,400))
    hack= pygame.image.load('hack.png')
    hacked= pygame.transform.scale(hack,(200,200))
    while True:
        game.blit(ai,(0,0))
        game.blit(hacked,(800,40))
        main("Press spacebar to start!",((0,0,0)),200,350)
        for e in pygame.event.get():
            if e.type== pygame.QUIT:
                pygame.quit()
            if e.type== pygame.KEYDOWN:
                if e.key== pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
def gameloop():
    exit= False
    x=0
    i=0
    d= 0
    y=200
    while not exit:
        game.fill((255,255,255))
        game.blit(trex,(i,0))
        game.blit(sin,(x,y))
        game.blit(trex,(i+700,0))
        game.blit(Cloud_SIZE,(100,30))
        game.blit(Cloud_SIZE,(250,150))
        game.blit(Cloud_SIZE,(350,80))
        if i<= -700:
            i=0
        i-=10
        d+=1
        main("Score:"+str(d),((0,0,0)),700,0)
        for e in pygame.event.get():
            if e.type== pygame.QUIT:
                exit= True
            
            
        pygame.display.update()
menu()