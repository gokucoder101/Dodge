import pygame
import math

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Dodge Ball")
font = pygame.font.Font(None, 75)
end_message = font.render("GAMEOVER", True, (205, 45, 84))
def end_message_initiantion():
    window.blit(end_message, (250, 250))
bam = 0
score = font.render(f"Score: {bam}", True, (255, 255, 255))
def show_score():
    window.blit(score, (400, 10))
#player
player_rect = pygame.Rect(400, 400, 60, 60)
player_x_change = 0
player_y_change = 0
def player():
    pygame.draw.rect(window, (255, 255, 255), player_rect)

#ball
ball_rect = pygame.Rect(0, 0, 60, 60)
ball_y_change = 7
ball_x_change = 7
def ball():
    pygame.draw.rect(window, (255, 0, 0), ball_rect)


running = True
while running:

    score = font.render(f"Score: {bam}", True, (255, 255, 255))
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y_change = -10
            if event.key == pygame.K_DOWN:
                player_y_change = 10
            if event.key == pygame.K_LEFT:
                player_x_change = -10
            if event.key == pygame.K_RIGHT:
                player_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change =0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    #Player
    player_rect.left += player_x_change
    player_rect.top += player_y_change
    if player_rect.left <= 0:
        player_rect.left = 0
    if player_rect.right >= 800:
        player_rect.right = 800
    if player_rect.bottom >= 700:
        player_rect.bottom = 700
    if player_rect.top <= 0:
        player_rect.top = 0
    

    #ball
    ball_rect.left += ball_x_change
    ball_rect.top += ball_y_change
    if ball_rect.left <= 0:
        ball_x_change *= -1
        bam += 1
    if ball_rect.right >= 800:
        ball_x_change *= -1
        bam += 1
    if ball_rect.bottom >= 700:
        ball_y_change *= -1
        bam += 1
    if ball_rect.top <= 0:
        ball_y_change *= -1
        bam += 1
    ball()
    player()
    if player_rect.colliderect(ball_rect):
        print("game over")
        end_message_initiantion()
        ball_x_change = 0
        player_x_change = 0
        player_y_change = 0
        ball_y_change = 0
    show_score()
    clock.tick(60)
    pygame.display.update()

        
