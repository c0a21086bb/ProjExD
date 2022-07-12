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
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkb1 = Bomb((255,0,0), 10, (+2,+3), scr)
    bkb2 = Bomb((0,255,0), 15, (+3,+2), scr)
    bkb3 = Bomb((0,0,255), 20, (+2,+2), scr)
    bkb4 = Bomb((255,255,0), 25, (+1,+2), scr)
    bkb5 = Bomb((255,0,255), 30, (+2,+1), scr)
    bkb6 = Bomb((0,255,255), 35, (+1,+1), scr)

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
        bkb4.update(scr)
        if kkt.rct.colliderect(bkb4.rct):
            return
        bkb5.update(scr)
        if kkt.rct.colliderect(bkb5.rct):
            return
        bkb6.update(scr)
        if kkt.rct.colliderect(bkb6.rct):
            return

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


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
