import pygame as pg

from settings import Settings as set

from pygame.sprite import Sprite
class Ball(Sprite):
    # This is the ball's class.

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving = False
        self.visible = False
        self.settings = set()
        self.velocity = self.settings.ball_speed
        self.accel = self.settings.ball_accel
        self.moving_down = True
        self.moving_left = False
        self.color = self.settings.ball_color
        self.Blue_paddle = ai_game.Blue_Paddle

        # self.image = pg.image.load('ball.bmp')
        # self.rect = self.image.get_rect()

        self.rect = pg.Rect((self.settings.screen_height / 2), (self.settings.screen_width / 2), self.settings.ball_size, self.settings.ball_size)

        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)

        #figure out the best way to have a constantly increasing speed thing.
    def Update(self, P1top, P1bottom, P2top, P2bottom):
        if self.moving:
            self.velocity = self.velocity * self.accel
            # if self.rect.top +2 > 0 and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.y += self.velocity
            else:
                self.y -= self.velocity
            # if self.rect.left +2 > 0 and self.rect.right < self.settings.screen_width:
            if self.moving_left:
                self.x -= self.velocity
            else:
                self.x += self.velocity
            if self.rect.top <= 0:
                self.moving_down = True
            elif self.rect.bottom >= self.settings.screen_height:
                self.moving_down = False
            if self.rect.right >= self.settings.screen_width -20:
                if self.rect.top >= P2top and self.rect.bottom <= P2bottom:
                    self.moving_left = True
            if self.rect.left <= 20:
                if self.rect.top >= P1top and self.rect.bottom <= P1bottom:
                    self.moving_left = False
        
        self.rect.x = self.x
        self.rect.y = self.y
    def draw_ball(self):
        """ draws the ball to the screen."""
        pg.draw.rect(self.screen, self.color, self.rect)