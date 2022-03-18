import os
from pygame import mixer
import random
import pygame

pygame.init()


w= 1200
h=500


red= (255,0,0)
black= (0,0,0)
white= (255,255,255)
blue= (0,0,255)
green= (0,255,0)

game= pygame.display.set_mode((w,h))
pygame.display.set_caption("Snakes")
pygame.display.update()
clock= pygame.time.Clock()
font= pygame.font.SysFont(None,55)




def main(text,color,x,y):
    sc= font.render(text,True,color)
    game.blit(sc, [x,y])

def plot(game,color,snk,size):
    for x, y in snk:
        pygame.draw.rect(game,color,[x,y,size,size])

def welcome():
  x=pygame.image.load("forest.jpg")
  pygame.display.flip()
  game.blit(x,(0,0))
  exit= False
  while not exit:

   main("Welcome to Snakes",green,400,200)
   main("Press Spacebar to continue",green,350,250)
   for events in pygame.event.get():
     if events.type== pygame.KEYDOWN:
          if events.key== pygame.K_SPACE:
              gameloop()
     if events.type == pygame.QUIT:
                    exit = True
   pygame.display.update()
   clock.tick(60)
def gameloop():
        mixer.music.load('background.wav')
        mixer.music.play()
        exit= False
        init_velocity=4
        over= False
        x= 40
        y= 30
        vx= 0
        vy= 0
        snk=[]
        snkl=1
        score= 0
        size=28
        with open('game.txt','r') as f:
            hs= f.read()
        fx= random.randint(20, w/2)
        fy= random.randint(20, h/2)
        fps=60
        while not exit:
            if over:
                
                with open('game.txt','w') as f:
                 f.write(str(hs))
                pygame.display.set_mode((1000,600))
                y=pygame.image.load('Death.jpg')
                pygame.display.flip()
                game.blit(y,(0,0))
                main("Game Over! Press Enter to continue",red,250,200)
                for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    exit = True

                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            else:
             
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit= True
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        vy= 0
                        vx= init_velocity
                    if event.key==pygame.K_LEFT:
                        vx= -init_velocity
                        vy= 0
            
                    if event.key==pygame.K_UP:
                        vx= 0
                        vy= -init_velocity
                
                    if event.key==pygame.K_DOWN:
                        vx= 0
                        vy= init_velocity
                    if event.key==pygame.K_a:
                        score+=100
             x= x+vx
             y= y+vy
             if abs(x-fx)<20 and abs(y-fy)<20:
                    
                    score =score+10
                    fx= random.randint(20, w/2)
                    fy= random.randint(20, h/2)
                    snkl+=5
                    if score>int(hs):
                        hs= score
                    
                    clock.tick(fps)
             game.fill(white)
             main("Score:" + str(score)+ "Hi Score:"+(str(hs)),red,5,5 )
             pygame.draw.rect(game,blue,[x,y,size,size])
             pygame.draw.rect(game,red,[fx,fy,size,size])

            
             head= []
             head.append(x)
             head.append(y)
             snk.append(head)
            
             if len(snk)>snkl:
                del snk[0]
            
             if head in snk[:-1]:
              over = True
              
             if x<0 or y<0 or x>w or y>h:
                over = True 
                
             plot(game,black,snk,size)
            
            pygame.display.update()
            clock.tick(fps)
         
        pygame.quit()
        quit()
welcome()
