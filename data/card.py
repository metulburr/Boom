class Card:
    def __init__(self, path, image):
        self.surf = image
        self.path = path
        self.rect = self.surf.get_rect()
        self.selected = False
