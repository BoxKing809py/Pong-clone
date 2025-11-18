# this has settings in it, crazy, huh?
class Settings:

    def __init__(self):
        #initalizes game settings.

        #screen settings.
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (23, 30, 23)
        self.paddle_speed = 4.0
        self.ball_speed = 2.0
        self.ball_accel = 1.0005
        self.ball_size = 30
        self.ball_color = (205, 255, 0)
        self.chaos_mode = False