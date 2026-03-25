# this has settings in it, crazy, huh?
class Settings:

    def __init__(self):
        #initalizes game settings.

        #screen settings.
        self.ssc = 1.25
        self.screen_width = (700 * self.ssc)
        self.screen_height = (500 * self.ssc)
        self.bg_color = (23, 30, 20)
        self.paddle_speed = 5.0
        self.ball_speed = 1.8
        self.ball_accel = 1.0006
        self.ball_size = 30
        self.ball_color = (125, 255, 0)
        self.chaos_mode = False