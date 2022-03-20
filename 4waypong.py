import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

#set up main window
screen_width = 1520
screen_height = 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('4 WAY PONG')

#game shapes
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
opponent2 = pygame.Rect(screen_width/2 - 90, 10, 280, 10)
opponent3 = pygame.Rect(screen_width/2 - 90, screen_height - 20, 280, 10)

bg_color = pygame.Color('grey12')
purple = (200, 100, 200)
green = (100, 200, 100)
red = (200, 0, 0)
blue = (0, 0, 255)


ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
opponent2_speed = 7
opponent3_speed = 7

player_score = 0
opponent_score = 0
opponent2_score = 0
opponent3_score = 0


#text setup
font = pygame.font.SysFont('couriernew', 100)


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, opponent2_score, opponent3_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.colliderect(opponent2) or ball.colliderect(opponent3):
        ball_speed_y *= -1
    if ball.top <= 0:
        ball_restart()
        opponent2_score -= 1
    if ball.bottom >= screen_height:
        ball_restart()
        opponent3_score -= 1
    if ball.left <= 0:
        ball_restart()
        opponent_score -= 1
    if ball.right >= screen_width:
        ball_restart()
        player_score -= 1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def opponent2_animation():
    
    if opponent2.center[0] < ball.x:
        opponent2.left += opponent2_speed
    if opponent2.center[0] > ball.x:
        opponent2.right -= opponent2_speed
    if opponent2.left <= 0:
        opponent2.left = 0
    if opponent2.right >= screen_width:
        opponent2.right = screen_width
        
def opponent3_animation():
    
    if opponent3.center[0] < ball.x:
        opponent3.left += opponent3_speed
    if opponent3.center[0] > ball.x:
        opponent3.right -= opponent3_speed
    if opponent3.left <= 0:
        opponent3.left = 0
    if opponent3.right >= screen_width:
        opponent3.right = screen_width

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()
    opponent2_animation()
    opponent3_animation()
    
    screen.fill(bg_color)
    player_text = font.render(str(player_score), True, purple)
    opponent_text = font.render(str(opponent_score), True, blue)
    opponent2_text = font.render(str(opponent2_score), True, green)
    opponent3_text = font.render(str(opponent3_score), True, red)
    screen.blit(player_text, (screen_width - 150, screen_height/2 - 50))
    screen.blit(opponent_text, (100, screen_height/2 - 50))
    screen.blit(opponent2_text, (screen_width/2 + 100, 100))
    screen.blit(opponent3_text, (screen_width/2 + 100, screen_height - 100))
    pygame.draw.rect(screen, purple, player)
    pygame.draw.rect(screen, blue, opponent)
    pygame.draw.rect(screen, green, opponent2)
    pygame.draw.rect(screen, red, opponent3)
    pygame.draw.ellipse(screen, purple, ball)
    pygame.draw.aaline(screen, purple, (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.aaline(screen, purple, (screen_width, screen_height/2), (0, screen_height/2))

    
                     
    pygame.display.update()
    clock.tick(90)

    
