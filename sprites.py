import pygame

pygame.init()

pygame.display.set_caption("Rocket in Space!")

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

#define the player sprite. Player starts at (0,0) point

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("character.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #keeping the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width 
        if self.rect.top < 0:
            self.rect.top = 0 
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height 
#end of class 

#creating all the sprites 
sprites = pygame.sprite.Group()

def start_game():
    #creating the object of player class
    player_1 = Player()
    sprites.add(player_1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        #get the set of keys that the user has pressed 
        pressed_keys = pygame.key.get_pressed()
        player_1.update(pressed_keys)

        screen.blit(pygame.image.load("background.png"), (0,0))
        sprites.draw(screen)
        pygame.display.update()

start_game()       