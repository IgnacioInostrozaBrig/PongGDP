import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)

# Paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_WIDTH = 25
ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)
ball_speed_x = 2
ball_speed_y = 2
speed_increment = 0.005

# Score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Initialize ball_color
ball_color = (255, 255, 255)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Control player 1 with keyboard
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 5

    # Control player 2 with mouse
    mouse_pos = pygame.mouse.get_pos()
    paddle2.y = mouse_pos[1] - PADDLE_HEIGHT // 2

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Collisions with the window edges
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Score handling
    if ball.left <= 0:
        score2 += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)
        ball_speed_x = 2
        ball_speed_y = 2
        ball_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    elif ball.right >= WIDTH:
        score1 += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)
        ball_speed_x = 2
        ball_speed_y = 2
        ball_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    # Gradually increase ball speed
    ball_speed_x += speed_increment
    ball_speed_y += speed_increment

    # Limit the frame rate to 60 frames per second using clock.tick(60)
    clock.tick(60)

    # Draw on the screen
    win.fill((0, 0, 0))
    pygame.draw.rect(win, WHITE, paddle1)
    pygame.draw.rect(win, WHITE, paddle2)
    pygame.draw.ellipse(win, ball_color, ball)  # Set the color to the random color
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()
