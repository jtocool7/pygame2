import pygame
pygame.init()

win = pygame.display.set_mode((1400,753))
pygame.display.set_caption("Jungle Adventure!")
bg = pygame.image.load('call.png')

#music = pygame.mixer.music.load('Our-Mountain_v003_Looping.mp3')
main = pygame.image.load('tile46.png')
sideright = pygame.image.load('tilej3.png')
dirtright = pygame.image.load('tile85.png')
dirtleft = pygame.image.load('tile800.png')
dirtwater = pygame.image.load('tile84.png')
sword2 = pygame.image.load('sword2.png')
dirtwater2 = pygame.image.load('tile86.png')
airtile = pygame.image.load('tile107.png')
sheild = pygame.image.load('sheild.png')
water1 = pygame.image.load('tile56.png')
sword = pygame.image.load('sword.png')
water = pygame.image.load('tile38.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

#pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
lol = True
big = True
cod = True
sheildd = False
trans1 = False
shoot = 0
spooth = 0
class player(object):
    def __init__(self, x,y ,width, height):
        self.x = x
        self.y = y 
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = True
        self.left = False
        self.walkCount = 0
        self.standing = True
        self.health = 20
        self.hitbox = (self.x + 17, self.y + 11, 29,52)
        self.cooldown = 0
        self.start = self.x
        self.start1 = self.y
        self.bottom = self.y + 60
    def draw(self,win):
        if sheildd == False:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if not(self.standing):   
                if self.right:
                     
                      win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                      self.walkCount += 1
                elif self.left:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1        
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
        if sheildd == True:
            win.blit(sheild,(self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29,52)
        pygame.draw.rect(win, (225,0,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,100,10))
        #self.bottom
        self.bottom = self.y + 60
        pygame.draw.rect(win, (225,0,0), (self.hitbox[0] - 35,self.y + 60,50,2))
        pygame.draw.rect(win, (225,0,0), (self.hitbox[0] - 35,self.y + 60,50,2))
        pygame.draw.rect(win, (0,225,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,50 -((50/10)* (10 - self.health)),10))
        #pygame.draw.rect(win, (225,0,0), self.hitbox,2)


man = player(48,710-64,64,64)
class projectile(object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 8 * facing
        self.stop1 = self.x + 50
        self.stop2 = self.x - 50
        self.point = (self.x, self.y)
        self.point2 = (self.x - 30, self.y)
    def draw(self,win):
        self.point = (self.x, self.y)
        self.point2 = (self.x + 30, self.y)
        if self.facing == 1: 
            win.blit(sword,(self.x,self.y))
            pygame.draw.circle(win,(225,0,0),(self.point2),5)
        if self.facing == -1:
            win.blit(sword2,(self.x,self.y))
            pygame.draw.circle(win,(225,0,0),(self.point),5)
        
def draw1():
    win.blit(bg, (0,0))
    text = font.render('Welcome To Jungle Adventure!',1,(225,0,0))
    text2 = font.render('Press The Space Bar To Continue',1,(225,0,0))
    win.blit(text,(1400/2 -150,735/2 + 10))
    win.blit(text2,(1400/2 -158,735/2 + 60))
    pygame.display.update()

def draw2():
    win.blit(bg, (0,0))
    win.blit(main,(48,710))
    win.blit(main,(96,710))
    win.blit(main,(144,710))
    win.blit(main,(192,710))
    win.blit(main,(240,710))
    win.blit(main,(288,710))
    win.blit(main,(336,710))
    win.blit(main,(384,710))
    win.blit(main,(432,710))
    win.blit(main,(480,710))
    win.blit(main,(528,710))
    win.blit(dirtwater,(528,710))
    win.blit(water,(576,710))
    win.blit(water,(624,710))
    win.blit(water,(672,710))
    win.blit(water,(710,710))
    win.blit(water,(758,710))
    win.blit(water,(806,710))
    win.blit(water,(854,710))
    win.blit(water,(902,710))
    win.blit(dirtwater,(528,518))
    win.blit(dirtwater,(528,566))
    win.blit(dirtwater,(528,614))
    win.blit(dirtwater,(528,662))
    win.blit(dirtwater2,(902,710))
    win.blit(dirtwater2,(902,518))
    win.blit(dirtwater2,(902,566))
    win.blit(dirtwater2,(902,614))
    win.blit(dirtwater2,(902,662))
    win.blit(water,(854,662))
    win.blit(water,(806,662))
    win.blit(water,(758,662))
    win.blit(water,(806,662))
    win.blit(water,(710,662))
    win.blit(water,(672,662))
    win.blit(water,(624,662))
    win.blit(water,(576,662))
    win.blit(sideright,(0,0))
    win.blit(sideright,(0,48))
    win.blit(water,(576,614))
    win.blit(water,(624,614))
    win.blit(water,(672,614))
    win.blit(water,(710,614))
    win.blit(water,(758,614))
    win.blit(water,(806,614))
    win.blit(water,(854,614))
    win.blit(water1,(576,566))
    win.blit(water1,(624,566))
    win.blit(water1,(672,566))
    win.blit(water1,(710,566))
    win.blit(water1,(758,566))
    win.blit(water1,(806,566))
    win.blit(water1,(854,566))
    win.blit(main,(576,518))
    win.blit(main,(624,518))
    win.blit(main,(670,518))
    #win.blit two middle(main,(758,518))
    win.blit(main,(806,518))
    win.blit(main,(854,518))
    win.blit(main,(998,710))
    win.blit(main,(950,710))
    win.blit(main,(1046,710))
    win.blit(main,(1094,710))
    win.blit(main,(1142,710))
    win.blit(main,(1190,710))
    win.blit(main,(1238,710))
    win.blit(main,(1286,710))
    win.blit(main,(1334,710))
    win.blit(dirtleft,(1353,710))
    win.blit(sideright,(0,96))
    win.blit(sideright,(0,144))
    win.blit(sideright,(0,192))
    win.blit(sideright,(0,240))
    win.blit(sideright,(0,288))
    win.blit(sideright,(0,336))
    win.blit(sideright,(0,384))
    win.blit(sideright,(0,432))
    win.blit(sideright,(0,480))
    win.blit(sideright,(0,528))
    win.blit(sideright,(0,576))
    win.blit(sideright,(0,585))
    win.blit(sideright,(0,624))
    win.blit(sideright,(0,672))
    win.blit(dirtright,(0,710))
    win.blit(airtile,(328,415))
    man.draw(win)
    #win.blit(sword,(48,710 - 64))
    for attacks in attack:
        attacks.draw(win)
    pygame.display.update()


   
def draw3():
    win.blit(bg,(0,0))
   
   
    text4 = font.render('Game Over!',1,(225,0,0))
    
    win.blit(text4,(1400/2 -50,735/2 + 60))
    pygame.display.update()
   

car = True
car2 = True
call = True
jag = True
floor1 = True
floor2 = False
waterFall = True
fall = False
big3 = False
mod = True
fall = False
floor3 = False
fa = False
fa2 = False
attack = []
count = 10
# main loop 1
font = pygame.font.SysFont('calibri',30,True)
big2 = False
while big and big2 == False and big3 == False:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        big = False
        big2 = True
   
    if lol == True:
        draw1()
#second and still not final loop
while big2 and big == False:
    trans1 = True
    y = man.y
    
    clock.tick(80)

    if shoot > 0:
        shoot += 1
    if shoot > 10:
        shoot = 0

    if spooth > 0:
        spooth += 1
    if spooth >= 300:
        spooth = 0

        
        
    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for attacks in attack:
        if attacks.x > attacks.stop2 and  attacks.x < attacks.stop1:
            attacks.x += attacks.vel
        else:
            attack.pop(attack.index(attacks))
        
    if keys[pygame.K_LEFT] and man.x > man.vel + 25 and fa2 == False and sheildd == False:
        if not(man.x <= 928 and man.x >= 928 - 48):
            
            
            man.x -= man.vel
            man.right = False
            man.left = True
            man.standing = False
        else:
            if man.isJump == True and car2 == True:
                
                man.x -= man.vel
                man.right = False
                man.left = True
                man.standing = False
            elif car2 == False:
                man.x -= man.vel
                man.right = False
                man.left = True
                man.standing = False
        if man.x < 928 and man.x > 928 - 48 and fall == False:
            car = True
                
        if floor2 == True:
            car2 = False
        if floor1 == False:
            man.x -= man.vel
            man.right = False
            man.left = True
            man.standing = False
            fa2 = False
        if fa2 == True and not(man.x >= 928 and man.x <= 928 - 48):
             man.x -= man.vel
             man.right = False
             man.left = True
             man.standing = False
        
            
    elif keys[pygame.K_LEFT] and man.x > man.vel + 25 and fa2 == True and sheildd == False:
        if fa2 == True and not(man.x <= 928 and man.x >= 928 - 48):
             man.x -= man.vel
             man.right = False
             man.left = True
             man.standing = False
    
    
            
                
          
    elif keys[pygame.K_RIGHT] and man.x < 1400 - man.width - man.vel and fa == False and sheildd == False and man.x < 1308: 
        if not(man.x >= 485 or man.x >= 485 + 48):
            
            
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            if man.isJump == True and car == True:
                
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
            elif car == False:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
        if man.x > 485 or man.x > 485 + 48 and fall == False:
            car = True
                
        if man.x > 563:
            car = False
        if floor1 == False:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
            fa = False
        if fa == True and not(man.x >= 485 or man.x >= 485 + 48):
             man.x += man.vel
             man.right = True
             man.left = False
             man.standing = False
        
            
    elif keys[pygame.K_RIGHT] and man.x < 1400 - man.width - man.vel and fa == True and sheildd == False:
        if fa == True and not(man.x >= 485 or man.x >= 485 + 48):
             man.x += man.vel
             man.right = True
             man.left = False
             man.standing = False

    
            
#and  == 410 + 45
             
        
            
                
    else:
        man.standing = True
        man.walkCount = 0
    if man.x >= 518 and man.x <= 624 and man.y == 448:
        floor1 = False
        floor2 = True
       
        man.isJump = False

        man = player(man.x,448 + 7,64,64)
        fall = False
    if man.x <= 928 and man.x > 928 - 48 - 48 and man.y == 448:
        floor1 = False
        floor2 = True
        man.isJump = False
        man = player(man.x,448 + 7,64,64)
        fall = False
    if man.y == 415 and man.x <= 268 and man.x >= 333:
        floor1 = False
        floor3 = True
        floor2 = False
        man.isJump = False

        man = player(man.x,415,64,64)
        fall = False

   
        
        
    
        
    
    
            
    if man.x >= 693 and man.x <= 768 and floor2 == True and waterFall == True and man.isJump == False:
        man.y -= (man.jumpCount ** 2) * 0.6 * neg
    if man.y >= 448 - man.hitbox[2]  and man.x >= 693 and man.x <= 768 and man.isJump == False:   
        big2 = False
        big3 = True
    
        
    if man.x <= 488 and man.y <= 710 - 64  and floor1 == False:
       fall = True
       if floor2 == True and fall == True:
           fa = True
           if count <= 710 - 64:
                  man.y -= (man.jumpCount ** 1) * 0.6 * -1
                  count -= 1
    if man.x >= 928 and man.y <= 710 - 64 and floor1 == False:
        fall = True
        if floor2 == True and fall == True:
            fa2 = True
            if count <= 710 - 64:
                man.y -= (man.jumpCount ** 1) * 0.6 * -1
                count -= 1
    

               
           
          
        
    if man.y >= 710 - 64:
        
        floor1 = True
        floor2 = True
        fall = False
        fa = False
        fa2 = False
        man.y = 710 - 64
        car2 = True
    #attack and defend
    if keys[pygame.K_d] and spooth < 200:
        timer = True
        if timer == True:
           spooth += 1
        sheildd = True
    else:
        if spooth >= 200:
           timer = True
        elif spooth <= 200:
            timer = False
            spooth = 0
        sheildd = False
    if spooth >= 200:
        timer = True
    if keys[pygame.K_a] and shoot == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(attack) < 2:
            #bulletSound.play()
            attack.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2),facing))
        shoot = 1
    
         
       
        
    
        
       
    
# man.y - (man.jumpCount ** 1) * 0.6 * neg        
    
        
    
        
        
    
                     
                     
                     
    if not(man.isJump) and call == True:
        if keys[pygame.K_UP] and fall == False and sheildd == False:
                
               
                
                
                man.isJump = True
                if man.right == True:
                   man.right = True
                if man.left == True:
                   man.left = True
                man.standing = False
                man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.6 * neg
            man.jumpCount -= 1
                
        
        else:
            man.isJump = False
            man.jumpCount = 10


    
       
   
   
    
        

    
       
   
        
        
        

    
        
                   
   
                     

                     
                     
                     
                     
                     
                     
    
    draw2()
    for attacks in attack:
        print(attacks.stop1)
    print(man.x)




while big3:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    draw3()
    keys = pygame.key.get_pressed()
    
    
    

  
