import pygame

from settings import Settings

class Blue_Paddle:
    # a class for the paddle.

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_up = False
        self.moving_down = False
        self.settings = Settings()


        self.image = pygame.image.load('blue_paddle.bmp')
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)
        self.y += ((self.settings.screen_height /2) - 30)

        self.rect.midleft = self.screen_rect.midleft
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        #updates paddle Y position.
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Red_Paddle:
    # a class for the paddle.

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_up = False
        self.moving_down = False
        self.ai_up = False
        self.ai_down = False
        self.settings = Settings()


        self.image = pygame.image.load('red_paddle.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.x += (self.settings.screen_width - 20)

        self.y = float(self.rect.y)
        self.y += ((self.settings.screen_height /2) -30)
        self.rect.midleft = self.screen_rect.midleft
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed
        if self.ai_up and self.rect.top >0:
            self.y -= (self.settings.paddle_speed -0.5)
        if self.ai_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += (self.settings.paddle_speed -0.5)

        #updates paddle Y position.
        self.rect.y = self.y
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)

