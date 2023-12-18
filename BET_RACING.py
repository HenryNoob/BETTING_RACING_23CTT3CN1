from tabnanny import NannyNag
from turtle import speed
import pygame, sys, random, os
from DinoRun import *
from pygame.locals import *
import time
from log import *
import re
from datetime import date, datetime

##########           00012112005000      MB             ##########

sys.path.insert(0, '../../')

WINDOWWIDTH = 1280
WINDOWHEIGHT = 720

# PHan backgroud menu
BG_MENU_IMG = pygame.image.load('img/backgroundMenu.png')
BG_PLAY_IMG = pygame.image.load("img/BackGroundPlay.png")
BG_MENU_SetAV = pygame.image.load("img/GiaoDienChonSetNV.png")
BG_Betting = pygame.image.load("img/GiaoDienBietting.png")
#BG_HELP_IMG = pygame.image.load('img/')
#BG_SHOP_IMG = pygame.image.load('img/')


b = [] # anh xe khi chien thang

a = [] # thu tu xe

bua_chu = [0, 0, 0]

# Hieu ung nut
NutPlay = pygame.image.load("img/NutPlay1.png")
NutHelp = pygame.image.load("img/NutHelp.png")
NutMiniGame = pygame.image.load("img/mini.png")
NutShop = pygame.image.load("img/shop.png")
NutAmthanh = pygame.image.load("img/NutAmThanh.png")
#Am thanh
menu_sound = pygame.mixer.Sound("sound/Rider_in_Thesky.mp3")
menu_sound.set_volume(0.8)
minigame_sound = pygame.mixer.Sound("sound/Cuckoo Clock - Quincas Moreira.mp3")
minigame_sound.set_volume(0.25)

pygame.init()

sold = load_sprites("img/", "sold_",3)

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.flip()
pygame.display.set_caption('RACING BETTING')

buff = load_sprites("img/Buff/", "m", 4)

#======================================================================================



RED = (255,0,0)
GREEN = (0,255,0)

WINDOWWIDTH = 1500
WINDOWHEIGHT = 700

X_MARGIN = 80
LANEWIDTH = 60

CARWIDTH = 0
CARHEIGHT = 0
CARSPEED = 2
CARIMG10 = pygame.image.load("img/dollar.png")



class Car1():

    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 250
        self.speed = CARSPEED * random.choice([1.1, 0.5, 1.0, 1.2, 0.7]) * random.choice([1.1, 0.5, 1.0, 1.2, 0.7])
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.buff = 1
        self.move = 0.5
        self.image_index = 0
        self.make = 0
        self.check = [True, True, True]
        self.time = [80, 80, 80]
        self.show = [0,0,0,0]
        self.pay = [False, False]
    def draw(self):
        DISPLAYSURF.blit(car_1[self.buff], (int(self.x), int(self.y)))
        if self.pay[0] or self.pay[1]:
            if self.pay[0] and self.pay[1]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/buadacbiet.png"), (int(self.x), int(self.y)))
            elif self.pay[0]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua.png"), (int(self.x), int(self.y)))
            else:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua2.png"), (int(self.x), int(self.y)))
        for i in range(3):
            if self.time[i] > 0 and self.check[i] == False:
                DISPLAYSURF.blit(buff[self.show[i]], (int(self.x), int(self.y)))
                self.time[i] -= 2
            
        if self.check[0]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (250, int(self.y) + 10))
        if self.check[1]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (550, int(self.y) + 10))
        if self.check[2]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (850, int(self.y) + 10))
        global pos_now1
        pos_now1 = self.x
        if (pos_now1 > 1151):
            a.append(1)
        if self.x == 1151 and a[0] == 1:
            self.make = (self.make + 1) % 100
            if self.make % 4 == 0:
                self.image_index = (self.image_index + 1) % 2
                self.buff = self.image_index + 1
    
    def apply_buff(self, buff_type):
        self.ngau_nhien = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
        for i in range(3):
            if buff_type == i:
                if self.ngau_nhien[i] >= 1 and self.ngau_nhien[i] <= 10:
                    self.x = 100
                    self.show[i] = 0
                elif self.ngau_nhien[i] >= 60 and self.ngau_nhien[i] <= 51:
                    self.x = 1100
                    self.show[i] = 1
                elif self.ngau_nhien[i] >= 11 and self.ngau_nhien[i] <= 50:
                    self.x += 100
                    self.speed *= 1.3
                    self.show[i] = 2
                else:
                    self.x -= 100
                    self.speed *= 0.8
                    self.show[i] = 3
    
    def update(self):
        global pos_now1
        pos_now1 = self.x
        if self.x <= 1150:
            if self.x + 5 > 1150:
                self.x += 5
            global vt_1
            vt_1 = 0
            if self.x >= 150 and self.x <= 200 and self.check[0]:
                self.apply_buff(0)
                self.check[0] = False
            elif self.x >= 450 and self.x <= 500 and self.check[1]:
                self.apply_buff(1)
                self.check[1] = False
            elif self.x >= 750 and self.x <= 800 and self.check[2]:
                self.apply_buff(2)
                self.check[2] = False
            else:
                self.x += self.speed  

        else:
            vt_1= 1
            self.x = 1151

class Car2():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 326
        self.speed = CARSPEED * random.choice([1.1, 0.5, 1.0, 1.2, 0.7])
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.buff = 1
        self.move = 0.5
        self.image_index = 0
        self.make = 0
        self.check = [True, True, True]
        self.time = [80, 80, 80]
        self.show = [0,0,0,0]
        self.pay = [False, False]
    def draw(self):
        DISPLAYSURF.blit(car_2[self.buff], (int(self.x), int(self.y)))
        if self.pay[0] or self.pay[1]:
            if self.pay[0] and self.pay[1]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/buadacbiet.png"), (int(self.x), int(self.y)))
            elif self.pay[0]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua.png"), (int(self.x), int(self.y)))
            else:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua2.png"), (int(self.x), int(self.y)))
        for i in range(3):
            if self.time[i] > 0 and self.check[i] == False:
                DISPLAYSURF.blit(buff[self.show[i]], (int(self.x), int(self.y)))
                self.time[i] -= 2
            
        if self.check[0]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (250, int(self.y) + 10))
        if self.check[1]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (550, int(self.y) + 10))
        if self.check[2]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (850, int(self.y) + 10))
        global pos_now2
        pos_now2 = self.x
        if (pos_now2 > 1151):
            a.append(2)
        if self.x == 1151 and a[0] == 2:
            self.make = (self.make + 1) % 100
            if self.make % 4 == 0:
                self.image_index = (self.image_index + 1) % 2
                self.buff = self.image_index + 1
    
    def apply_buff(self, buff_type):
        self.ngau_nhien = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
        for i in range(3):
            if buff_type == i:
                if self.ngau_nhien[i] >= 1 and self.ngau_nhien[i] <= 10:
                    self.x = 100
                    self.show[i] = 0
                elif self.ngau_nhien[i] >= 60 and self.ngau_nhien[i] <= 51:
                    self.x = 1100
                    self.show[i] = 1
                elif self.ngau_nhien[i] >= 11 and self.ngau_nhien[i] <= 50:
                    self.x += 100
                    self.speed *= 1.3
                    self.show[i] = 2
                else:
                    self.x -= 100
                    self.speed *= 0.8
                    self.show[i] = 3
    def update(self):
        global pos_now2
        pos_now2 = self.x
        if self.x <= 1150:
            if self.x +5 > 1150:
                self.x += 8
            global vt_2
            vt_2 = 0
            if self.x >= 150 and self.x <= 200 and self.check[0]:
                self.apply_buff(0)
                self.check[0] = False
            elif self.x >= 450 and self.x <= 500 and self.check[1]:
                self.apply_buff(1)
                self.check[1] = False
            elif self.x >= 750 and self.x <= 800 and self.check[2]:
                self.apply_buff(2)
                self.check[2] = False
            else:
                self.x += self.speed  

        else:
            vt_2 = 2
            self.x = 1151
            
class Car3():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 417
        self.speed = CARSPEED * random.choice([1.1, 0.5, 1.0, 1.2, 0.7])
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.buff = 1
        self.move = 0.5
        self.image_index = 0
        self.make = 0
        self.check = [True, True, True]
        self.time = [80, 80, 80]
        self.show = [0,0,0,0]
        self.pay = [False, False]
    def draw(self):
        DISPLAYSURF.blit(car_3[self.buff], (int(self.x), int(self.y)))
        if self.pay[0] or self.pay[1]:
            if self.pay[0] and self.pay[1]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/buadacbiet.png"), (int(self.x), int(self.y)))
            elif self.pay[0]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua.png"), (int(self.x), int(self.y)))
            else:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua2.png"), (int(self.x), int(self.y)))
        for i in range(3):
            if self.time[i] > 0 and self.check[i] == False:
                DISPLAYSURF.blit(buff[self.show[i]], (int(self.x), int(self.y)))
                self.time[i] -= 2
            
        if self.check[0]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (250, int(self.y) + 10))
        if self.check[1]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (550, int(self.y) + 10))
        if self.check[2]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (850, int(self.y) + 10))
        global pos_now3
        pos_now3 = self.x
        if (pos_now3 > 1151):
            a.append(3)
        if self.x == 1151 and a[0] == 3:
            self.make = (self.make + 1) % 100
            if self.make % 4 == 0:
                self.image_index = (self.image_index + 1) % 2
                self.buff = self.image_index + 1
    
    def apply_buff(self, buff_type):
        self.ngau_nhien = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
        for i in range(3):
            if buff_type == i:
                if self.ngau_nhien[i] >= 1 and self.ngau_nhien[i] <= 10:
                    self.x = 100
                    self.show[i] = 0
                elif self.ngau_nhien[i] >= 60 and self.ngau_nhien[i] <= 51:
                    self.x = 1100
                    self.show[i] = 1
                elif self.ngau_nhien[i] >= 11 and self.ngau_nhien[i] <= 50:
                    self.x += 100
                    self.speed *= 1.3
                    self.show[i] = 2
                else:
                    self.x -= 100
                    self.speed *= 0.8
                    self.show[i] = 3
    def update(self):
        global pos_now3
        pos_now3 = self.x
        if self.x <= 1150:
            if self.x +5 > 1150:
                self.x += 8
            global vt_3
            vt_3 = 0
            if self.x >= 150 and self.x <= 200 and self.check[0]:
                self.apply_buff(0)
                self.check[0] = False
            elif self.x >= 450 and self.x <= 500 and self.check[1]:
                self.apply_buff(1)
                self.check[1] = False
            elif self.x >= 750 and self.x <= 800 and self.check[2]:
                self.apply_buff(2)
                self.check[2] = False
            else:
                self.x += self.speed  

        else:
            vt_3 = 3
            self.x = 1151


class Car4():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 502
        self.speed = CARSPEED * random.choice([1.1, 0.5, 1.0, 1.2, 0.7])
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.buff = 1
        self.move = 0.5
        self.image_index = 0
        self.make = 0
        self.check = [True, True, True]
        self.time = [80, 80, 80]
        self.show = [0,0,0,0]
        self.pay = [False, False]
    def draw(self):
        DISPLAYSURF.blit(car_4[self.buff], (int(self.x), int(self.y)))
        if self.pay[0] or self.pay[1]:
            if self.pay[0] and self.pay[1]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/buadacbiet.png"), (int(self.x), int(self.y)))
            elif self.pay[0]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua.png"), (int(self.x), int(self.y)))
            else:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua2.png"), (int(self.x), int(self.y)))
        for i in range(3):
            if self.time[i] > 0 and self.check[i] == False:
                DISPLAYSURF.blit(buff[self.show[i]], (int(self.x), int(self.y)))
                self.time[i] -= 2
            
        if self.check[0]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (250, int(self.y) + 10))
        if self.check[1]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (550, int(self.y) + 10))
        if self.check[2]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (850, int(self.y) + 10))
        global pos_now4
        pos_now4 = self.x
        if (pos_now4 > 1151):
            a.append(4)
        if self.x == 1151 and a[0] == 4:
            self.make = (self.make + 1) % 100
            if self.make % 4 == 0:
                self.image_index = (self.image_index + 1) % 2
                self.buff = self.image_index + 1
    
    def apply_buff(self, buff_type):
        self.ngau_nhien = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
        for i in range(3):
            if buff_type == i:
                if self.ngau_nhien[i] >= 1 and self.ngau_nhien[i] <= 10:
                    self.x = 100
                    self.show[i] = 0
                elif self.ngau_nhien[i] >= 60 and self.ngau_nhien[i] <= 51:
                    self.x = 1100
                    self.show[i] = 1
                elif self.ngau_nhien[i] >= 11 and self.ngau_nhien[i] <= 50:
                    self.x += 100
                    self.speed *= 1.3
                    self.show[i] = 2
                else:
                    self.x -= 100
                    self.speed *= 0.8
                    self.show[i] = 3
    def update(self):
        global pos_now4
        pos_now4 = self.x
        if self.x <= 1150:
            if self.x +5 > 1150:
                self.x += 8
            global vt_4
            vt_4 = 0
            if self.x >= 150 and self.x <= 200 and self.check[0]:
                self.apply_buff(0)
                self.check[0] = False
            elif self.x >= 450 and self.x <= 500 and self.check[1]:
                self.apply_buff(1)
                self.check[1] = False
            elif self.x >= 750 and self.x <= 800 and self.check[2]:
                self.apply_buff(2)
                self.check[2] = False
            else:
                self.x += self.speed 

        else:
            vt_4 = 4
            self.x = 1151
class Car5():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 584
        self.speed = CARSPEED * random.choice([1.1, 0.5, 1.0, 1.2, 0.7])
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
        self.buff = 1
        self.move = 0.5
        self.image_index = 0
        self.make = 0
        self.check = [True, True, True]
        self.time = [80, 80, 80]
        self.show = [0,0,0,0]
        self.pay = [False, False]
    def draw(self):
        DISPLAYSURF.blit(car_5[self.buff], (int(self.x), int(self.y)))
        if self.pay[0] or self.pay[1]:
            if self.pay[0] and self.pay[1]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/buadacbiet.png"), (int(self.x), int(self.y)))
            elif self.pay[0]:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua.png"), (int(self.x), int(self.y)))
            else:
                DISPLAYSURF.blit(pygame.image.load("img/Buff/bua2.png"), (int(self.x), int(self.y)))
        for i in range(3):
            if self.time[i] > 0 and self.check[i] == False:
                DISPLAYSURF.blit(buff[self.show[i]], (int(self.x), int(self.y)))
                self.time[i] -= 2
            
        if self.check[0]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (250, int(self.y) + 10))
        if self.check[1]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (550, int(self.y) + 10))
        if self.check[2]:
            DISPLAYSURF.blit(pygame.image.load("img/Buff/hop qua bi an.png"), (850, int(self.y) + 10))
        global pos_now5
        pos_now5 = self.x
        if (pos_now5 > 1151):
            a.append(5)
        if self.x == 1151 and a[0] == 5:
            self.make = (self.make + 1) % 100
            if self.make % 4 == 0:
                self.image_index = (self.image_index + 1) % 2
                self.buff = self.image_index + 1
    
    def apply_buff(self, buff_type):
        self.ngau_nhien = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
        for i in range(3):
            if buff_type == i:
                if self.ngau_nhien[i] >= 1 and self.ngau_nhien[i] <= 10:
                    self.x = 100
                    self.show[i] = 0
                elif self.ngau_nhien[i] >= 60 and self.ngau_nhien[i] <= 51:
                    self.x = 1100
                    self.show[i] = 1
                elif self.ngau_nhien[i] >= 11 and self.ngau_nhien[i] <= 50:
                    self.x += 100
                    self.speed *= 1.3
                    self.show[i] = 2
                else:
                    self.x -= 100
                    self.speed *= 0.8
                    self.show[i] = 3
    def update(self):
        global pos_now5
        pos_now5 = self.x
        if self.x <= 1150:
            if self.x +5 > 1150:
                self.x += 8
            global vt_5
            vt_5 = 0
            if self.x >= 150 and self.x <= 200 and self.check[0]:
                self.apply_buff(0)
                self.check[0] = False
            elif self.x >= 450 and self.x <= 500 and self.check[1]:
                self.apply_buff(1)
                self.check[1] = False
            elif self.x >= 750 and self.x <= 800 and self.check[2]:
                self.apply_buff(2)
                self.check[2] = False
            else:
                self.x += self.speed

        else:
            vt_5 = 5
            self.x = 1151

def scrshoot():
        current_datetime = datetime.now()
        date_time_str = current_datetime.strftime("%H-%M_%d-%m-%Y")
        scrshoot_file_path = f"screenshot_folder/img-{date_time_str}.jpg"
        capture_region = (0, 0, 1280, 720)
        captured_surface = DISPLAYSURF.subsurface(pygame.Rect(capture_region))
        pygame.image.save(captured_surface, scrshoot_file_path)

def gamePlay(bg, car1, car2, car3, car4, car5):
    tmp = 10
    global  coin, tienCuoc
    global bua_chu
    car1.__init__()
    car2.__init__()
    car3.__init__()
    car4.__init__()
    car5.__init__()
    bg.__init__()
    bg.count_321()
    running = True
    cars = [car1, car2, car3, car4, car5]
    for i, car in enumerate(cars, start=1):
        if (bua_chu[0] >= 1 or bua_chu[1] >= 1 or bua_chu[2] >= 1) and chon_xe[0] == i:
            if bua_chu[0] >= 1:
                car.speed *= ((100 + 1 * bua_chu[0]) % 100)
                bua_chu[0] -= bua_chu[0]
                car.pay[0] = True
            
            if bua_chu[1] >= 1:
                car.speed *= ((100 + 3 * bua_chu[1]) % 100)
                bua_chu[1] -= bua_chu[1]
                car.pay[1] = True
            
            if bua_chu[2] >= 1:
                car.x += 100 * bua_chu[2]
                bua_chu[2] -= bua_chu[2]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.draw()
        car1.draw()
        car1.update()
        car2.draw()
        car2.update()
        car3.draw()
        car3.update()
        car4.draw()
        car4.update()
        car5.draw()
        car5.update()
        if (vt_1==1 and vt_2==2 and vt_3== 3 and vt_4==4 and vt_5==5):

            if (chon_xe[0]== a[0]):
                over_bg = pygame.image.load("img\giaodienWWin.png")
                DISPLAYSURF.blit(over_bg, (0, 0))
                draw_text("PRESS 'ESC' TO RETURN MAINMENU", "font/FZ-SG ZT Voltra.ttf", 30, (255, 255, 255), 1050, 640, "topright")
                draw_text("PRESS 'T' TO SCREENSHOT THE RANKING", "font/FZ-SG ZT Voltra.ttf", 30, (255, 255, 255), 1120, 670, "topright")
                if ( tmp == 10):
                    coin[0] += int(tienCuoc[0]) * 10
                    tmp += 10
            else:
                over_bg = pygame.image.load("img\giaodienOver.png")
                DISPLAYSURF.blit(over_bg, (0, 0))
                draw_text("PRESS 'ESC' TO RETURN MAINMENU", "font/FZ-SG ZT Voltra.ttf", 30, (255, 255, 255), 1050, 640, "topright")
                draw_text("PRESS 'T' TO SCREENSHOT THE RANKING", "font/FZ-SG ZT Voltra.ttf", 30, (255, 255, 255), 1120, 670, "topright")
                if (tmp == 10 ):
                    coin[0] -= int(tienCuoc[0])
                    tmp += 10
            file_2 = open(coin_username_info, 'w')
            file_2.write(str(coin[0]))
            file_2.close()
            for i in range(5):
                if i == 0:
                    DISPLAYSURF.blit(b[a[i] - 1][1], (504, 239))
                if i == 1:
                    DISPLAYSURF.blit(b[a[i] - 1][1], (373, 291))
                if i == 2:
                    DISPLAYSURF.blit(b[a[i] - 1][1], (650, 335))
                if i == 3:
                    DISPLAYSURF.blit(b[a[i] - 1][1], (231, 379))
                if i == 4:
                    DISPLAYSURF.blit(b[a[i] - 1][1], (787, 417))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    a.clear()
                    b.clear()
                    menu_sound.stop()
                    MeNu()
                elif event.key == K_t:
                    # Gọi hàm scrshoot khi phím 'T' được nhấn
                    scrshoot()
        pygame.display.update()
        fpsClock.tick(FPS)

def start_the_game():
    bg = Back_ground()
    car1 = Car1()
    car2 = Car2()
    car3 = Car3()
    car4 = Car4()
    car5 = Car5()
    gamePlay(bg, car1, car2, car3, car4, car5)
#######################################################




def drawCoin():  # vẽ tiền
    draw_text(str(coin[0]) + "$", "font/monofonto.ttf", 48, (255, 255, 255), 1180, 450, "topright")
    DISPLAYSURF.blit(CARIMG10, (0, 0))
    
def drawCoin_1():  # vẽ tiền
    draw_text(str(coin[0]) + "$", "font/monofonto.ttf", 48, (255, 255, 255), 890, 640, "topright")
    DISPLAYSURF.blit(pygame.image.load("img/coin.png"), (0, 0))


def draw_Race(race_img): #hàm vẽ đường đua
    DISPLAYSURF.blit(race_img, 0, 0)



#ve cac giao dien
def HamGiaoDienSetNV():
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Quay lại
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                #chon nut tick thu nhat
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 270) & (mouse_y <= 328):
                    HamGiaoDienBetting(1)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 340) & (mouse_y <= 398):
                    HamGiaoDienBetting(2)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 417) & (mouse_y <= 478):
                    HamGiaoDienBetting(3)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 487) & (mouse_y <= 549):
                    HamGiaoDienBetting(4)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 566) & (mouse_y <= 624):
                    HamGiaoDienBetting(5)

        DISPLAYSURF.blit(BG_MENU_SetAV, (0, 0))

        # Hieu ung nut
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 270) & (mouse_y <= 328):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet1.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 340) & (mouse_y <= 398):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet2.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 417) & (mouse_y <= 478):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet3.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 487) & (mouse_y <= 549):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet4.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 566) & (mouse_y <= 624):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet5.png"), (0, 0))
        pygame.display.update()


FONT = pygame.font.Font("font/monofonto.ttf", 32)
tienCuoc = [0]
class InputBox:
    def __init__(self, x, y, w, h, text= '' ):
        global tienCuoc
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color((0, 0, 0))
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color((255, 255, 255)) if self.active else pygame.Color((0, 0, 0))
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        DISPLAYSURF.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect, 2)


def HamGiaoDienBetting(set):
    global  chon_xe
    chon_xe = [1]
    global car_1, car_2, car_3, car_4, car_5, tienCuoc
    if (set == 1):
        car_1 = load_sprites("img/Set Xe/Set 1/", "nph_",3, 200, 88)
        car_2 = load_sprites("img/Set Xe/Set 1/", "tdth_",3, 200, 88)
        car_3 = load_sprites("img/Set Xe/Set 1/", "nvbd_",3, 200, 88)
        car_4 = load_sprites("img/Set Xe/Set 1/", "tnd_",3, 200, 88)
        car_5 = load_sprites("img/Set Xe/Set 1/", "hau_",3, 200, 88)
    elif (set == 2):
        car_1 = load_sprites("img/Set Xe/Set 2/", "nph_",3, 200, 88)
        car_2 = load_sprites("img/Set Xe/Set 2/", "tdth_",3, 200, 88)
        car_3 = load_sprites("img/Set Xe/Set 2/", "nvbd_",3, 200, 88)
        car_4 = load_sprites("img/Set Xe/Set 2/", "tnd_",3, 200, 88)
        car_5 = load_sprites("img/Set Xe/Set 2/", "hau_",3, 200, 88)
    elif (set == 3):
        car_1 = load_sprites("img/Set Xe/Set 3/", "nph_",3, 200, 88)
        car_2 = load_sprites("img/Set Xe/Set 3/", "tdth_",3, 200, 88)
        car_3 = load_sprites("img/Set Xe/Set 3/", "nvbd_",3, 200, 88)
        car_4 = load_sprites("img/Set Xe/Set 3/", "tnd_",3, 200, 88)
        car_5 = load_sprites("img/Set Xe/Set 3/", "hau_",3, 200, 88)
    elif (set == 4):
        car_1 = load_sprites("img/Set Xe/Set 4/", "nph_",3, 200, 88)
        car_2 = load_sprites("img/Set Xe/Set 4/", "tdth_",3, 200, 88)
        car_3 = load_sprites("img/Set Xe/Set 4/", "nvbd_",3, 200, 88)
        car_4 = load_sprites("img/Set Xe/Set 4/", "tnd_",3, 200, 88)
        car_5 = load_sprites("img/Set Xe/Set 4/", "hau_",3, 200, 88)
    elif (set == 5):
        car_1 = load_sprites("img/Set Xe/Set 5/", "nph_",3, 200, 88)
        car_2 = load_sprites("img/Set Xe/Set 5/", "tdth_",3, 200, 88)
        car_3 = load_sprites("img/Set Xe/Set 5/", "nvbd_",3, 200, 88)
        car_4 = load_sprites("img/Set Xe/Set 5/", "tnd_",3, 200, 88)
        car_5 = load_sprites("img/Set Xe/Set 5/", "hau_",3, 200, 88)

    b.append(car_1)
    b.append(car_2)
    b.append(car_3)
    b.append(car_4)
    b.append(car_5)

    Nut1 = False
    Nut2 = False
    Nut3 = False
    Nut4 = False
    Nut5 = False
    clock = pygame.time.Clock()
    input_box = InputBox(680, 458, 140, 42)  # Khai bao cai hop
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        DISPLAYSURF.blit(BG_Betting, (0, 0))
        draw_text(" Enter your stake: ", "font/monofonto.ttf", 38, (255, 255, 255), 680, 453, "topright")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            input_box.handle_event(event)
            # Quay lại
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                global choose_1, choose_2, choose_3, choose_4, choose_5
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                # Chon nut 1

                if (event.button == 1) & (mouse_x >= 334) & (mouse_x <= 396) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = True
                    Nut2 = False
                    Nut3 = False
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 1
                # Chon nut 2
                if (event.button == 1) & (mouse_x >= 471) & (mouse_x <= 532) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = True
                    Nut3 = False
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 2
                # chon nut 3
                if (event.button == 1) & (mouse_x >= 606) & (mouse_x <= 668) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = True
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 3
                # Chon nut 4
                if (event.button == 1) & (mouse_x >= 751) & (mouse_x <= 810) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = False
                    Nut4 = True
                    Nut5 = False
                    chon_xe[0] = 4
                if (event.button == 1) & (mouse_x >= 888) & (mouse_x <= 950) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = False
                    Nut4 = False
                    Nut5 = True
                    chon_xe[0] = 5
                if tienCuoc[0] == '':
                    print('')
                elif (int(tienCuoc[0]) <= int(coin[0])) & (int(tienCuoc[0]) > 0) & (event.button == 1) & (mouse_x >= 570) & (mouse_x <= 754) & (mouse_y >= 540) & (mouse_y <= 607):
                    start_the_game()

        # in set nhan vat ra
        if set == 1:
            DISPLAYSURF.blit(pygame.image.load("img/Set 1.png"), (0, 0))
        if set == 2:
            DISPLAYSURF.blit(pygame.image.load("img/Set 2.png"), (0, 0))
        if set == 3:
            DISPLAYSURF.blit(pygame.image.load("img/Set 3.png"), (0, 0))
        if set == 4:
            DISPLAYSURF.blit(pygame.image.load("img/Set 4.png"), (0, 0))
        if set == 5:
            DISPLAYSURF.blit(pygame.image.load("img/Set 5.png"), (0, 0))

        input_box.update()
        # Hieu ung chon
        if Nut1 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick1.png"), (0, 0))
        elif Nut2 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick2.png"), (0, 0))
        elif Nut3 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick3.png"), (0, 0))
        elif Nut4 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick4.png"), (0, 0))
        elif Nut5 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick5.png"), (0, 0))

            # Hieu ung nut
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 334) & (mouse_x <= 396) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick1.png"), (0, 0))
        if (mouse_x >= 471) & (mouse_x <= 532) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick2.png"), (0, 0))
        if (mouse_x >= 606) & (mouse_x <= 668) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick3.png"), (0, 0))
        if (mouse_x >= 751) & (mouse_x <= 810) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick4.png"), (0, 0))
        if (mouse_x >= 888) & (mouse_x <= 950) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick5.png"), (0, 0))
        if (mouse_x >= 570) & (mouse_x <= 754) & (mouse_y >= 540) & (mouse_y <= 607):
            DISPLAYSURF.blit(pygame.image.load("img/NutStart.png"), (0, 0))

        input_box.draw(DISPLAYSURF)
        tienCuoc[0] = input_box.text
        drawCoin_1()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

#############################################################################
class Back_ground():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = map
        #self.width = self.img.get_width()
        #self.height = self.img.get_height()

    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        #DISPLAYSURF.blit(self.img, (int(self.x), int(self.y - self.height)))

    def count_321(self):
        count = 3
        while count >= 0:
            DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
            if count == 0:
                message_display("GO!", 100, -70, (0, 255, 255), 1)
            elif count == 3:
                message_display(str(count), 100, -70, (255,0,0), 0.75)
            elif count == 2:
                message_display(str(count), 100, -70, (255, 255, 0), 0.75)
            elif count == 1:
                message_display(str(count), 100, -70, (0, 255, 0), 0.75)
            count -= 1
        fpsClock.tick(FPS)
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, shift_x, shift_y, color, sleep_time):
    largeText = pygame.font.SysFont('comicsansms', 72, True)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((WINDOWWIDTH / 2 - shift_x), (WINDOWHEIGHT / 2 - shift_y))
    DISPLAYSURF.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(sleep_time)



#############################################################################3

def HamGiaoDienHelp():
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
        DISPLAYSURF.blit(pygame.image.load("img/GiaodienHelp.png"), (0, 0))
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        pygame.display.update()


def HamGiaoDienShop():
    check_1 = True
    check_2 = True
    check_3 = True
    global bua_chu
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                if (coin[0] >= 300) & (event.button == 1) & (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 236) & (mouse_y <= 292):
                    check_1 = False
                    coin[0] -= 300
                    bua_chu[0] += 1
                if (coin[0] >= 500) & (event.button == 1) & (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 322) & (mouse_y <= 377):
                    check_2 = False
                    coin[0] -= 500
                    bua_chu[1] += 1
                if (coin[0] >= 2000) & (event.button == 1) & (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 409) & (mouse_y <= 469):
                    check_3 = False
                    coin[0] -= 2000
                    bua_chu[2] += 1
        DISPLAYSURF.blit(pygame.image.load("img/GiaoDienShop.png"), (0, 0))
        drawCoin()
        if check_1 == False:
            DISPLAYSURF.blit(sold[0], (0, 0))
            drawCoin()
        if check_2 == False:
            DISPLAYSURF.blit(sold[1], (0, 0))
            drawCoin()
        if check_3 == False:
            DISPLAYSURF.blit(sold[2], (0, 0))
            drawCoin()
        if (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 236) & (mouse_y <= 292):
            DISPLAYSURF.blit(pygame.image.load("img/Mua1.png"), (0, 0))
        if (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 322) & (mouse_y <= 377):
            DISPLAYSURF.blit(pygame.image.load("img/Mua2.png"), (0, 0))
        if (mouse_x >= 953) & (mouse_x <= 1013) & (mouse_y >= 409) & (mouse_y <= 469):
            DISPLAYSURF.blit(pygame.image.load("img/Mua3.png"), (0, 0))
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        pygame.display.update()

def HamGiaoDienPlay():
    global map,car1,car2,car3,car4,car5
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Quay lại
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                # chon Map
                if (event.button == 1) & (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 460) & (mouse_y <= 690):
                    map=pygame.image.load("img/Map1.png")
                    HamGiaoDienSetNV()
                if (event.button == 1) & (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 158) & (mouse_y <= 392):
                    map=pygame.image.load("img/Map5.png")
                    HamGiaoDienSetNV()
                if (event.button == 1) & (mouse_x >= 428) & (mouse_x <= 847) & (mouse_y >= 289) & (mouse_y <= 527):
                    map=pygame.image.load("img/Map3.png")
                    HamGiaoDienSetNV()
                if (event.button == 1) & (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 151) & (mouse_y <= 392):
                    map=pygame.image.load("img/Map4.png")
                    HamGiaoDienSetNV()
                if (event.button == 1) & (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 455) & (mouse_y <= 720):
                    map=pygame.image.load("img/Map2.png")
                    HamGiaoDienSetNV()


        DISPLAYSURF.blit(BG_PLAY_IMG, (0, 0)) # Background sau khi ấn nút Play
        # Bên dưới là hiệu ứng nút Play
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 460) & (mouse_y <= 690):
            DISPLAYSURF.blit(pygame.image.load("img/NutChonseMap1.png"), (0, 0))
        if (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 158) & (mouse_y <= 392):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap5.png"), (0, 0))
        if (mouse_x >= 428) & (mouse_x <= 847) & (mouse_y >= 289) & (mouse_y <= 527):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap3.png"), (0, 0))
        if (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 151) & (mouse_y <= 392):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap4.png"), (0, 0))
        if (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 455) & (mouse_y <= 720):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap2.png"), (0, 0))

        pygame.display.update()

def MeNu():
    menu_sound.play(-1) # Bât nhạc menu
    vcl = 1
    global coin
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) & (coin[0] > 0) & (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 185) &( mouse_y <= 242): #vào play
                    HamGiaoDienPlay()
                if (event.button == 1) & (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 278) & ( mouse_y <= 337):
                    HamGiaoDienShop()
                if (event.button == 1) & (coin[0] == 0) & (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 374) & ( mouse_y <= 433):
                    # print("MiniGame")
                    menu_sound.stop()
                    minigame_sound.play()
                    start_game(coin)
                    file_2 = open(coin_username_info, 'w')
                    file_2.write(str(coin[0]))
                    file_2.close()
                    minigame_sound.stop()
                    menu_sound.play(-1)
                if (event.button == 1) & (mouse_x >= 553) & (mouse_x <= 639) & (mouse_y >= 448) &( mouse_y <= 535):
                    HamGiaoDienHelp()
                if (event.button == 1) & (mouse_x >= 648) & (mouse_x <= 725) & (mouse_y >= 448) &( mouse_y <= 535):
                    vcl *= -1
                    if vcl == -1:
                        menu_sound.set_volume(0)
                    else:
                        menu_sound.set_volume(0.8)

        DISPLAYSURF.blit(BG_MENU_IMG, (0, 0))
        drawCoin()

        # Chỗ này làm hiệu ứn nút
        if (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 185) &( mouse_y <= 242):
            DISPLAYSURF.blit(NutPlay, (0, 0))
        if (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 278) & ( mouse_y <= 337):
            DISPLAYSURF.blit(NutShop, (0, 0))
        if (mouse_x >= 491) & (mouse_x <= 788) & (mouse_y >= 374) & ( mouse_y <= 433):
            DISPLAYSURF.blit(NutMiniGame, (0, 0))
        if (mouse_x >= 553) & (mouse_x <= 639) & (mouse_y >= 448) &( mouse_y <= 535):
            DISPLAYSURF.blit(NutHelp, (0, 0))
        if (mouse_x >= 648) & (mouse_x <= 725) & (mouse_y >= 448) &( mouse_y <= 535):
            DISPLAYSURF.blit(NutAmthanh, (0, 0))
        pygame.display.update()

def main():
    MeNu()

from tkinter import *
import os


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def delete5():
    screen6.destroy()


def delete6():
    screen7.destroy()


def delete7():
    screen8.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=delete2).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def otp_incorrect():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Success")
    screen6.geometry("150x100")
    Label(screen6, text="OTP is incorrect").pack()
    Button(screen6, text="OK", command=delete5).pack()

def username_or_password():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Success")
    screen7.geometry("400x100")
    Label(screen7, text="The length of Username or Password must be more than 6 characters !").pack()
    Button(screen7, text="OK", command=delete6).pack()


def gmail_incorrect():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Success")
    screen8.geometry("150x100")
    Label(screen8, text="Gmail is not correct!").pack()
    Button(screen8, text="OK", command=delete7).pack()



def register_user():
    # print("working")
    global username_info
    username_info = username.get()
    password_info = password.get()
    
    if not ((len(username_info)<6 or len(password_info)<6 or ' ' in username_info or ' ' in password_info)):
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        global coin_username_info
        coin_username_info =username_info+"_coin"
        file_1 = open(coin_username_info, "w")
        file_1.write("")
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
    else:
        username_or_password()

         

global ma_otp
ma_otp = generate_verification_code()
# ma otp sai do kieu du lieu khac nhau, can xu xu ly kieu du lieu cua ham sinh ngau nhien 

def login_verify():
    

    username1 = username_verify.get()
    password1 = password_verify.get()
    otp1 = otp_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        global  coin_username_info
        coin_username_info=username1+"_coin"
        if password1 in verify:
            if str(ma_otp) == str(otp1):
                global coin
                coin = []
                # Mở file để đọc
                try:
                    file_1 = open(coin_username_info, 'r')
                    n = file_1.read()
                    file_1.close()
                    # Kiểm tra nếu file rỗng
                    if not n:
                        coin.append(50)  # Nếu file rỗng, gán giá trị mặc định là 50
                    else:
                        coin.append(int(n))
                except FileNotFoundError:
                    print(f"File {coin_username_info} not found.")
                    # Xử lý trường hợp file không tồn tại, có thể tạo mới file hoặc thực hiện xử lý khác
                if __name__ == '__main__':
                    main()
            else:
                otp_incorrect()

        else:
            password_not_recognised()

    else:
        user_not_found()
    


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def is_valid_gmail(email):
    gmail_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@gmail\.com$')
    if gmail_pattern.match(email):
        return True
    else:
        return False

def send_otp():

    email1 = email_verify.get()
    # email_entry1.delete(0, END)
    if is_valid_gmail(email1):
        send_email(email1, ma_otp)

        Label(screen2, text="OTP * ").pack()
        otp_entry1 = Entry(screen2, textvariable=otp_verify)
        otp_entry1.pack()
        Label(screen2, text="").pack()


        Label(screen2, text="").pack()
        Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
        Label(screen2, text="").pack()
    else:
        gmail_incorrect()




def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x400")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    global email_verify
    global otp_verify

    global email_entry1
    global otp_entry1


    username_verify = StringVar()
    password_verify = StringVar()
    email_verify = StringVar()
    otp_verify = StringVar()
 
    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Email * ").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()

    Label(screen2, text="").pack()
    # chinh sua cho nay gui email chu khong phai la login verify
    Button(screen2, text="Send OTP", width=10, height=1, command=send_otp).pack()
    Label(screen2, text="").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("LOGIN SCREEN")
    Label(text="WELCOME TO BETTING_RACING", bg="#FFCCFF", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()



''''''''''''''''''''''''''''''
'  Nhóm 1                    '
'  Game: Cá cược đua xe      '
'                            '
'                            '
'  GVHD: VÕ HOÀNG QUÂN       '
'                            '
'  +   NGUYỄN PHÚC HẬU       '
'                            '
'  +   TỐNG DƯƠNG THÁI HÒA   '
'                            '
'  +   NGUYỄN PHÚC HOÀNG     '
'                            '
'  +   NGUYỄN VĂN BÌNH DƯƠNG '
'                            '
'  +   TRẦN NHẬT DƯƠNG       '
'                            '
'                            '
''''''''''''''''''''''''''''''