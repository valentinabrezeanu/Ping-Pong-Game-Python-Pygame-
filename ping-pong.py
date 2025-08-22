import pygame
import sys

# Inițializare pygame
pygame.init()

# Setări ecran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

# Culorile
white=(255, 255, 255)
blue = (0, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
mov=(255,0,255)
# Parametrii jocului
paddle_width = 15
paddle_height = 100
ball_size = 20

# Poziția paletelor
paddle1 = pygame.Rect(50, (screen_height - paddle_height) / 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(screen_width - 50 - paddle_width, (screen_height - paddle_height) / 2, paddle_width, paddle_height)
ball = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)

# Viteza paletelor și a mingii
paddle_speed = 8
ball_speed_x = 5
ball_speed_y = 5

# Scoruri
score1 = 0
score2 = 0

# Font pentru scor
font = pygame.font.Font(None, 74)

clock = pygame.time.Clock()

def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, blue, paddle1)
    pygame.draw.rect(screen, red, paddle2)
    pygame.draw.ellipse(screen, mov, ball)
    
    # Scor
    score_text = font.render(f"{score1} - {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 50))
    
    pygame.display.flip()

def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < screen_height:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < screen_height:
        paddle2.y += paddle_speed

def move_ball():
    global ball_speed_x, ball_speed_y, score1, score2
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= screen_width:
        score1 += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= -1

# Bucla principală a jocului
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_paddles()
    move_ball()
    draw_objects()
    clock.tick(60)