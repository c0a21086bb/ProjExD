import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("よけろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    bmimg_sfc1 = pg.Surface((20, 20))  #小さくて速い爆弾
    bmimg_sfc1.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc1, (0, 0, 255), (10, 10), 10)
    bmimg_rct1 = bmimg_sfc1.get_rect()
    bmimg_rct1.centerx = random.randint(0, screen_rct.width)
    bmimg_rct1.centery = random.randint(0, screen_rct.height)

    bmimg_sfc2 = pg.Surface((50, 50))   #大きくて遅い爆弾
    bmimg_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc2, (0, 255, 0), (25, 25), 25)
    bmimg_rct2 = bmimg_sfc2.get_rect()
    bmimg_rct2.centerx = random.randint(0, screen_rct.width)
    bmimg_rct2.centery = random.randint(0, screen_rct.height)

    bmimg_sfc3 = pg.Surface((1000, 1000))  #特大爆弾　横移動のみ　反射しない
    bmimg_sfc3.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc3, (255, 0, 0), (500, 500), 500)
    bmimg_rct3 = bmimg_sfc3.get_rect()
    bmimg_rct3.centerx = -1000
    bmimg_rct3.centery = 200

    bmimg_sfc4 = pg.Surface((1000, 1000))  #特大爆弾　横移動のみ　反射しない
    bmimg_sfc4.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc4, (255, 0, 0), (500, 500), 500)
    bmimg_rct4 = bmimg_sfc4.get_rect()
    bmimg_rct4.centerx = -3000
    bmimg_rct4.centery = 700

    vx1, vy1 = 5, 5    #小さくて速い爆弾の速度
    vx2, vy2 = 3, 3    #大きくて遅い爆弾の速度
    vx3, vy3 = 1, 0    #特大爆弾の速度


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()   #速度変更
        if key_states[pg.K_UP] == True:
            kkimg_rct.centery -= 5
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 5
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 5
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 5
        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP] == True:
                kkimg_rct.centery += 5
            if key_states[pg.K_DOWN] == True:
                kkimg_rct.centery -= 5
            if key_states[pg.K_LEFT] == True:
                kkimg_rct.centerx += 5
            if key_states[pg.K_RIGHT] == True:
                kkimg_rct.centerx -= 5
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        bmimg_rct1.move_ip(vx1, vy1)
        bmimg_rct2.move_ip(vx2, vy2)
        bmimg_rct3.move_ip(vx3, vy3)
        bmimg_rct4.move_ip(vx3, vy3)

        screen_sfc.blit(bmimg_sfc4, bmimg_rct4)
        screen_sfc.blit(bmimg_sfc3, bmimg_rct3)
        screen_sfc.blit(bmimg_sfc2, bmimg_rct2)
        screen_sfc.blit(bmimg_sfc1, bmimg_rct1)

        yoko, tate = check_bound(bmimg_rct1, screen_rct)
        vx1 *= yoko
        vy1 *= tate

        yoko, tate = check_bound(bmimg_rct2, screen_rct)
        vx2 *= yoko
        vy2 *= tate

        if kkimg_rct.colliderect(bmimg_rct1):
            pg.display.update
            clock.tick(0.2)
            return

        if kkimg_rct.colliderect(bmimg_rct2):
            pg.display.update
            clock.tick(0.2)
            return

        if kkimg_rct.colliderect(bmimg_rct3):
            pg.display.update
            clock.tick(0.2)
            return
        
        if kkimg_rct.colliderect(bmimg_rct4):
            pg.display.update
            clock.tick(0.2)
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    yoko, tate = +1, +1 
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()