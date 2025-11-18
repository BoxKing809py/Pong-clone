import sys

import pygame as pg

from random import choice

from random import randint

from settings import Settings

from paddle import Blue_Paddle

from paddle import Red_Paddle

from ball import Ball
class Pongclone:
    # class for all of the game.

    def __init__(self):
        pg.init()
        #self.screen = pg.display.set_mode((640, 480), pg.RESIZABLE)
        pg.display.set_caption("PongClone tm")
        self.settings = Settings()
        self.balls = pg.sprite.Group()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.scoreright = 0
        self.scoreleft = 0  
        self.clock = pg.time.Clock()
        self.Blue_Paddle = Blue_Paddle(self)
        self.P2 = Red_Paddle(self)
        self.Ball = Ball(self)

        self.multiplayer = False
        

        
    def run_game(self):
        # Main loop that keeps the game flowing.
        while True:
            self._check_events()
            self.Blue_Paddle.update()
            self.P2.update()
            self.Ball.Update(self.Blue_Paddle.rect.top, self.Blue_Paddle.rect.bottom, self.P2.rect.top, self.P2.rect.bottom)
            for activeball in self.balls.copy():
                if self.multiplayer == False:
                    activeball.rect.y = self.Ball.rect.y
                    activeball.rect.x = self.Ball.rect.x
                if activeball.rect.right <= 0:
                    self.balls.remove(activeball)
                    if self.multiplayer == False:
                        self.Ball.moving = False
                    self.scoreright +=1
                    print(f"Red, {self.scoreright}")
                if activeball.rect.left >= self.settings.screen_width:
                    self.balls.remove(activeball)
                    if self.multiplayer == False:
                        self.Ball.moving = False
                    self.scoreleft +=1
                    print(f"Blue, {self.scoreleft}")
            if self.multiplayer == False:
                if self.Ball.visible != False:
                    if self.Ball.rect.centery < self.P2.rect.centery:
                        self.P2.ai_up = True
                        self.P2.ai_down = False
                    elif self.Ball.rect.centery > self.P2.rect.centery:
                        self.P2.ai_down = True
                        self.P2.ai_up = False
                    else:
                        self.P2.ai_up = False
                        self.P2.ai_down = False
            else:
                self.P2.ai_down = False
                self.P2.ai_up = False

            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        # respond to key preses
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pg.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        #move P1.
        if event.key == pg.K_w:
            self.Blue_Paddle.moving_up = True
        elif event.key == pg.K_s:
            self.Blue_Paddle.moving_down = True
        #move P2.
        if self.multiplayer:
            if event.key == pg.K_UP:
                self.P2.moving_up = True
            elif event.key == pg.K_DOWN:
                self.P2.moving_down = True
        if event.key == pg.K_q:
            print(f"Blue | {self.scoreleft} - {self.scoreright} | Red")
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._start_game()
        elif event.key == pg.K_m:
            self.multiplayer = True
    def _check_keyup_events(self, event):
        if event.key == pg.K_w:
            self.Blue_Paddle.moving_up = False
        if event.key == pg.K_s:
            self.Blue_Paddle.moving_down = False
        #stop moving P2.
        if event.key == pg.K_UP:
            self.P2.moving_up = False
        elif event.key == pg.K_DOWN:
            self.P2.moving_down = False
    def _start_game(self):
        if self.multiplayer == False:
            if len(self.balls.copy()) <= 0:
                self._create_ball()
        elif self.multiplayer:
            self._create_ball()
        # self._create_ball()
    def _update_screen(self):
         # updates the screen and displays it.
            self.screen.fill(self.settings.bg_color)
            self.Blue_Paddle.blitme()
            self.P2.blitme()
            self.text_display()
            if self.Ball.moving == True and self.Ball.visible == True:
                for activeballs in self.balls.sprites():
                    activeballs.moving = True
                    if self.settings.chaos_mode:
                        activeballs.moving_down = choice([True, False])
                        activeballs.moving_left = choice([True, False])
                    activeballs.draw_ball()
                    activeballs.Update(self.Blue_Paddle.rect.top, self.Blue_Paddle.rect.bottom, self.P2.rect.top, self.P2.rect.bottom)
            pg.display.flip()
    def _create_ball(self):
        # Creates a new ball, and attempts to set all the variables/booleans properly.
        new_ball = Ball(self)
        self.Ball.visible = True
        self.Ball.moving = True
        new_ball.moving_down = choice([True, False])
        new_ball.moving_left = choice([True, False])
        new_ball.velocity += (randint(1,20)/10)
        self.balls.add(new_ball)
        self.Ball.velocity = (self.settings.ball_speed)
        self.Ball.y = (self.settings.screen_height / 2)
        self.Ball.x = (self.settings.screen_width / 2)
    
    def text_display(self):
        # Draws the  instructions and Score to the screen.
        font = pg.font.Font(None, 20)
        font2 = pg.font.Font(None, 42)
        text = font.render("W/S or UP/DOWN(P2) to move paddles, SPACE to summon balls, M to enable P2, Q to Quit", True, (225, 225, 245))
        score = font2.render(f"Blue | {self.scoreleft} - {self.scoreright} | Red", True, (255,155,255))
        textpos = text.get_rect(centerx=self.settings.screen_width / 2, y=20)
        scorepos = score.get_rect(centerx=self.settings.screen_width / 2, centery=self.settings.screen_height/2)
        self.screen.blit(text, textpos)
        self.screen.blit(score, scorepos)


if __name__ == '__main__':
    #run the game.
    ai = Pongclone()
    ai.run_game()
