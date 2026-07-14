from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Camra():
    def __init__(self):
        self.x=0
        self.y=0

    def update(self, player):
        self.x = player.x - SCREEN_WIDTH//2
        self.y = player.y - SCREEN_HEIGHT//2