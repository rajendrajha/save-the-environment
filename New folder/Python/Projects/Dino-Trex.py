import pygame
pygame.init()
exit= False
i= 0
x= 0
y= 240
score= 0
game= pygame.display.set_mode((1200,500))
pygame.display.set_caption("Dino-Trex")
Dino= pygame.image.load('dinot.png')
Trex= pygame.transform.scale(Dino,(150,80))
GROUND= pygame.image.load('ground.png')
GROUND_SIZE= pygame.transform.scale(GROUND,(1200,20))


font= pygame.font.SysFont(None,55)
def text(text,color,x,y):
    st= font.render(text,True,color)
    game.blit(st,[x,y])

while not exit:
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           exit= True
       if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_SPACE:
               y-=100
               x+=10
       if event.type==pygame.KEYUP:
           if event.key==pygame.K_SPACE:
               y+=100
       if x>0:
           x=0
   score+=1
   game.fill((255,255,255))
   i-=0.3
   game.blit(GROUND_SIZE,(i,300))
   game.blit(GROUND_SIZE,(i+1200,300))
   if i<=-1200:
       i=0
   game.blit(Trex,(x,y))
   
   text("Score:"+str(score),((0,0,0)),900,10)
   #240-50=190

   pygame.display.update()
pygame.quit()
quit()