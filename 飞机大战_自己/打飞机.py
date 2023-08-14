import pygame
import random
import math

#1. 初始化界面
pygame.init()
scree = pygame.display.set_mode((800,600))
pygame.display.set_caption('打飞机游戏')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')

#添加背景音效
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1) #单曲循环
#创建射中音效
bao_sound = pygame.mixer.Sound('exp.wav')

#5.飞机
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 500 
playerStep = 0 #玩家移动的速度

#分数  
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
#font = pygame.font.SysFont('simsunnsimsun',32)  
def show_score():
    text = f'Score:{score}'
    score_render = font.render(text,True,(0,255,0))
    scree.blit(score_render,(10,10))

#游戏结束
is_over = False
over_font = pygame.font.Font('freesansbold.ttf',64)
def check_is_over():
    if is_over:
        text = 'Game Over'
        score_render = over_font.render(text,True,(255,0,0))
        scree.blit(score_render,(220,250))

#9. 添加敌人
number_of_enemies = 6 #敌人的数量

#敌人类
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(200,600)
        self.y = random.randint(50,250)
        self.step = 1 #敌人移动速度
    #当被射中时，恢复位置
    def reset(self):
        self.x = random.randint(200,600)
        self.y = random.randint(50,200)

enemies = [] #保存所有的敌人
for i in range(number_of_enemies):
    enemies.append(Enemy())

#两个点之间的距离
def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a+b*b) #开根号


#子弹类
class Bullet():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')
        self.x = playerX + 22 
        self.y = playerY -10
        self.step = 2 #子弹移动速度
    #击中
    def hit(self):
        global score
        for e in enemies:
            if(distance(self.x,self.y,e.x,e.y) < 30):
                #射中了
                bao_sound.play()
                bullets.remove(self)
                e.reset() 
                score += 1
                print(score)

bullets = [] #保存现有子弹

#显示并移动子弹
def show_bullets():
    for b in bullets:
        scree.blit(b.img,(b.x,b.y))
        b.hit() #发射子弹
        b.y -= b.step #移动子弹
        #判断子弹是否出界面，如果出界就移除
        if b.y < 0: 
            bullets.remove(b)


#显示敌人，实现敌人的移动和下沉
def show_enemy():
    global is_over
    for e in enemies:
        scree.blit(e.img,(e.x,e.y))
        e.x += e.step
        if(e.x > 736 or e.x < 0):
            e.step *= -1
            e.y += 40
            if e.y > 450:
                is_over = True
                print('游戏结束啦')
                enemies.clear()

def move_player():
    global playerX
    playerX += playerStep
    #防止飞机出界
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

#2. 游戏主循环
running = True
while running:
    scree.blit(bgImg,(0,0))
    show_score() #显示分数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #通过键盘事件控制飞机的移动
        if event.type == pygame.KEYDOWN: #按下就移动
            if event.key == pygame.K_RIGHT:
                playerStep = 1.5
            elif event.key == pygame.K_LEFT:
                playerStep = -1.5
            elif event.key == pygame.K_SPACE:
                print('发射子弹....')
                #创建一颗子弹
                bullets.append(Bullet())

        if event.type == pygame.KEYUP: #抬起来就不动
            playerStep = 0
    scree.blit(playerImg,(playerX,playerY))
    move_player() #移动玩家
    show_enemy() #显示敌人
    show_bullets()#显示子弹
    check_is_over()#显示游戏结束字段
    pygame.display.update()