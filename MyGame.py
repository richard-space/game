# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:49:50 2018

@author: 益慶
"""

import pygame
import random
import time

#Boss類別
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.boss=boss   #boss圖片
        self.positions=(140,30)
        self.rect = self.boss.get_rect() #取得BOSS圖片大小
        self.rect.center=(140,30)
        
    def point(self,surf):#設定位置
        global railgun
        sound=random.randint(0,100)       
        directx= random.randint(-30,30)
        directy= random.randint(-20,20)
        new_pt=self.positions[0]+directx,self.positions[1]+directy
        if (new_pt[0]>0 and new_pt[0]<=250) and (new_pt[1]>0 and new_pt[1]<=200):#判斷是否在指定範圍內
            self.positions=(new_pt)
            if sound<6:#隨機發起攻擊與吼叫
                railgun=Xray(self.positions)
                allsprite.add(railgun)
                railgun.draw(surf)
                lion.play()
        self.rect.center=self.positions
        
    def draw(self,surf):
        surf.blit(self.boss, self.positions)

#邊界類別       
class Bound(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.positions=(200,15)
        self.rect = pygame.Rect(0,0,400,30)
        self.rect.center=(200,15)       

#飛機類別
class Planes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.planes=planes  #飛機圖片
        self.positions=(180,500)
        self.rect = self.planes.get_rect()  #取得飛機圖片大小
                
        
    def point(self, pt):#設定位置         
         new_pt=self.positions[0]+pt[0],self.positions[1]+pt[1]
         if (new_pt[0]>0 and new_pt[0]<=360) and (new_pt[1]>0 and new_pt[1]<=500):#判斷是否在指定範圍內
             self.positions=(new_pt)
             self.rect.center=self.positions
             
    def draw(self,surf):
        surf.blit(self.planes, self.positions)
  
#子彈類別             
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pt):
        pygame.sprite.Sprite.__init__(self)
        self.bull = bull
        self.entities = {}
        self.entity_id = 0
        self.positions=pt
        self.rect = self.bull.get_rect()
        self.rect.center=pt
        
    def point(self,obj):#設定位置
        soundhit.play()
        self.positions = (obj.positions[0]+5,obj.positions[1]-10)
        self.entity_id+=1
        self.entities[self.entity_id]=self.positions

#雷電類別        
class Xray(pygame.sprite.Sprite):
    def __init__(self,pt):
        pygame.sprite.Sprite.__init__(self)
        self.xray = xray
        self.positions=(pt[0],pt[1]+100)
        self.rect = self.xray.get_rect()
        self.rect.center=self.positions
        
        
    def draw(self,surf):
        surf.blit(self.xray, self.positions)
        
       
#畫出子彈
def draw_bullet(obj,surf):
    global bullets
    i=0
    for pt in obj.entities.values():
        i+=1
        if pt[1]-30>0:
            pt=(pt[0],pt[1]-30)
            obj.entities[i]=pt
            surf.blit(obj.bull, pt)
            bullets.add(Bullet(pt))
            allsprite.add(bullets)
   
#開始遊戲畫面
def startGame(): 
    global running ,background,state
    background.fill((255,255,255))          
    text = font1.render("Game Start !!", 1, (255,0,255))  #顯示訊息
    background.blit(text, (screen.get_width()/2-100,screen.get_height()/2-20))
    screen.blit(background, (0,0))
    pygame.display.update()  #更新畫面            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state=False
        if event.type == pygame.KEYDOWN:
            running = True
            state=False

#結束遊戲畫面              
def gameover(message,score):  
    global running ,background,state
    pygame.mixer.stop()#停止播放音效
    background.fill((255,255,255))          
    text = font1.render(message, 1, (255,0,255))  #顯示訊息
    text2 = font2.render("Your Score : "+str(score), 1, (255,0,0))#顯示分數
    background.blit(text, (screen.get_width()/2-100,screen.get_height()/2-20))
    background.blit(text2, (screen.get_width()/2-100,screen.get_height()/2+10))
    screen.blit(background, (0,0))
    pygame.display.update()  #更新畫面
    time.sleep(3)  #暫停3秒
    running = False  #結束程式              


FPS = 20  #幀數設定
pygame.init()
fpsClock=pygame.time.Clock()
score = 0 
life=100
font = pygame.font.SysFont("arial", 28)   #文字區塊
font1 = pygame.font.SysFont("arial", 28)
font2 = pygame.font.SysFont("arial", 28)
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 560
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #設定畫面大小
pygame.display.set_caption("射擊遊戲")   #設定視窗標題
background = pygame.Surface(screen.get_size())   #設定背景
background = background.convert()
background.fill((255,255,255))
soundhit = pygame.mixer.Sound("hit.wav")   #載入音效
bomb = pygame.mixer.Sound("bomb.wav")
lion=pygame.mixer.Sound("lion1.wav")
back=pygame.image.load("back.gif").convert_alpha()    #載入圖片
planes=pygame.image.load("plane.png").convert_alpha()
boss=pygame.image.load("boss.png").convert_alpha()
bull=pygame.image.load("bullet.png").convert_alpha()
xray=pygame.image.load("xray.png").convert_alpha()
background.blit(back, (0,0))
screen.blit(background, (0,0))
allsprite = pygame.sprite.Group() 
bullets = pygame.sprite.Group()
railgun=Xray((140,30))
running = False
state=True

clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

#飛機移動的方向&步長
UP    = (0, -10)
DOWN  = (0, 10)
LEFT  = (-10, 0)
RIGHT = (10, 0)
 
#初始化
if __name__ == '__main__':
    Planes=Planes()
    bullet=Bullet((180,500))
    Boss=Boss()
    Bound=Bound()
    allsprite.add(Planes)
    allsprite.add(Boss)
    allsprite.add(Bound)
     
    while state:
        startGame()#遊戲開始介面
    
    while running:
        fpsClock.tick(FPS)
       
        for event in pygame.event.get():    #設定功能按鍵
            if event.type == pygame.QUIT:
                running=False             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Planes.point(UP)
                elif event.key == pygame.K_DOWN:
                    Planes.point(DOWN)
                elif event.key == pygame.K_LEFT:
                    Planes.point(LEFT)
                elif event.key == pygame.K_RIGHT:
                    Planes.point(RIGHT)                    
                        
        background.fill((255,255,255))
        background.blit(back, (0,0))
        bullet.point(Planes)
        Boss.point(background)
        hit = pygame.sprite.spritecollide(Boss, bullets,True)#偵測子彈與BOSS發生碰撞
        pygame.sprite.spritecollide(Bound, bullets,True)#偵測子彈與邊界發生碰撞
        if len(hit)>0:  #子彈與BOSS發生碰撞時加分
            bomb.play()
            score+=len(hit)
            
        lifestr="life  "+str(life)
        life_show=font1.render(lifestr, 1,(0,255,0))
        msgstr = "score   " + str(score)
        msg = font.render(msgstr, 1,(255,0,0))
        background.blit(msg, (10,10))
        background.blit(life_show, (10,500))
        Boss.draw(background)
        draw_bullet(bullet,background)
        Planes.draw(background)
        screen.blit(background, (0,0))
        pygame.display.update()
        bosshit = pygame.sprite.collide_rect(Planes,railgun )
        if bosshit:  #飛機與雷電發生碰撞時減血
            life-=1
            if life<=0:
                gameover("Game Over",score)#遊戲結束
        
  
pygame.quit()