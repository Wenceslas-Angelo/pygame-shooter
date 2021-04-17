import pygame
from game import Game
import math

pygame.init()

#Create window
pygame.display.set_caption("Comet fall game")
icon = pygame.image.load("assets/banner.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1080,620))
background = pygame.image.load("assets/bg.jpg")

#Banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil( screen.get_width() / 4)

#Button
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = banner.get_rect()
play_button_rect.x = math.ceil( screen.get_width() / 3.33)
play_button_rect.y = math.ceil( screen.get_height() / 1.7)

#charge game
game = Game()

#Boucle infinite
running = True
while running:
    screen.blit(background, (0, -300))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        # if exit
        if event.type == pygame.QUIT:
            running = False

        #if keyboard is pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #Touch space detected
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        #if keyboard is not pressed
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        #mouse event button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

