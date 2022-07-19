from hashlib import blake2b
import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 2
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 2
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 2
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 2
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 2
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 2
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 2
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 2
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = 0
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        
        # 練習5
        self.blit(scr)          

class Score:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = scr.rct.width
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        
        # 練習5
        self.blit(scr)


def main():
    score = 0
    clock = pg.time.Clock()
    scr = Screen("がんばれ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkb1 = Bomb((255,0,0), 10, (+0,+1), scr)
    bkb2 = Bomb((255,0,0), 10, (+0,+2), scr)
    bkb3 = Bomb((255,0,0), 10, (+0,+3), scr)
    score1 = Score((0,0,255), 10, (-1,0), scr)
    score2 = Score((0,0,255), 10, (-2,0), scr)
    score3 = Score((0,0,255), 10, (-3,+0), scr)

    while True:
        scr.blit()
        
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkb1.update(scr)
        if kkt.rct.colliderect(bkb1.rct):
            return
        bkb2.update(scr)
        if kkt.rct.colliderect(bkb2.rct):
            return
        bkb3.update(scr)
        if kkt.rct.colliderect(bkb3.rct):
            return
        score1.update(scr)
        if kkt.rct.colliderect(score1.rct):
            score += 1
        score2.update(scr)
        if kkt.rct.colliderect(score2.rct):
            score += 1
        score3.update(scr)
        if kkt.rct.colliderect(score3.rct):
            score += 1

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

def new_score(rct, scr_rct):
    if rct.left < scr_rct.left:
        yoko = 1600
        tate = random.randint(0, 900)
        return yoko, tate

def new_bomb(rct, scr_rct):
    if scr_rct.bottom < rct.bottom:
        yoko = random.randint(0, 1600)
        tate = 900
        return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
