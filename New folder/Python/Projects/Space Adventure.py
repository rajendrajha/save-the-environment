import pygame
import random
from pygame import mixer
x= pygame.init()
print(x)
exit= False

x= 100
y= 450
init_velocity= 0

game=pygame.display.set_mode((450,600))
mixer.music.load('background.wav')
mixer.music.play()
pygame.display.set_caption("Space Adventures")
rocket=pygame.image.load('R.png')
r= pygame.transform.scale(rocket,(150,150))
r2= pygame.transform.rotate(r,50)
space= pygame.image.load('space3.jpg')
s= pygame.transform.scale(space,(450,600))
alien=[]
enemy_x=[]
enemy_y=[]
enemy_x_velocity=[]
enemy_y_velocity=[]
noe= 6
for i in range(noe):
    alien.append(pygame.transform.scale(pygame.image.load('ghost.png'),(50,50)))
    enemy_x.append(random.randint(0,200))
    enemy_y.append(random.randint(50,250))
    enemy_x_velocity.append(4)
    enemy_y_velocity.append(40)

def enemy(x,y,i):
    game.blit(alien[i],(x,y))

def player(x,y):    
    game.blit(r2,(x,y))



    
while not exit:
    game.fill((0,0,0))
    for e in pygame.event.get():
       
        if e.type== pygame.QUIT:
            exit= True
        if e.type== pygame.KEYDOWN:
            if e.key==pygame.K_SPACE:
                init_velocity=0.3
            
    x= x+init_velocity
    
    
    if x<= -75:
        x= -75
        init_velocity=0.3
    if x>=320:
        x= 320
        init_velocity=-0.3
    for i in range(noe):
        enemy_x[i] += enemy_x_velocity[i]
        if enemy_x[i] <= 0:
            enemy_x_velocity[i] = 4
            enemy_y[i] +=enemy_x_velocity[i]
        elif enemy_x[i] >= 736:
            enemy_x_velocity[i] = -4
            enemy_y[i] += enemy_y_velocity[i]
        enemy(enemy_x[i],enemy_y[i],i)
    game.blit(s,(0,0))
    
    player(x,y)
    
    pygame.display.update()



pygame.quit()
quit()