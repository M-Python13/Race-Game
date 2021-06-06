from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,image_player,x_player, y_player,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(20,20))
        self.speed = player_speed
        self.rect  = self.image.get_rect()
        self.rect.x= x_player 
        self.rect.y= y_player

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed

class Opponent(GameSprite):                                 
    def update(self):
        self.rect.x -= self.speed
        
class Finish(sprite.Sprite):
    def __init__(self,colour1,colour2,colour3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.colour1= colour1
        self.colour2= colour2
        self.colour3= colour3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((colour1,colour2,colour3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500


font.init()
font = font.SysFont('Arial', 25)


player = Player("player.png", 650, 100,randint(1,3))
opponent = Opponent("opponent.png",650,400,1) 

finish_line = Finish(255, 229, 0, 100, 0 , 20 , 500)

window = display.set_mode((win_width, win_height))
display.set_caption("Race Game")
background = transform.scale(image.load("background.jpg"), (700,500))      

mixer.init()
mixer.music.load("Jasmin.mp3")
mixer.music.play()

clock = time.Clock()
FPS = 60
clock.tick(FPS)

game = True
finished = False
while game:

    for e in event.get():
        keys_pressed = key.get_pressed()
        if e.type == QUIT:
            game = False

    if finished != True:
        window.blit(background, (0,0))
        player.update()
        opponent.update()
        
        player.reset()
        opponent.reset()

        finish_line.draw_wall()

        text_win = font.render("YOU WIN!", 1 ,(0,177,0))
        text_lose = font.render("YOU LOSE!", 1, (255,0,0))
        text_howto = font.render("Use 'W' or the 'Up Arrow Key to move forward!", 1 ,(0,0,0))
        
        window.blit(text_howto,(150,0))

        if sprite.collide_rect(player,finish_line):
            window.blit(text_win, (275,450)) 
            finished = True
        if sprite.collide_rect(finish_line,opponent): 
            window.blit(text_lose, (275,450)) 
            finished = True

    display.update()