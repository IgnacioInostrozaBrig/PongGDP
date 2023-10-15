import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound effects
pygame.mixer.init()

# Load the sound files
collide_sound = pygame.mixer.Sound("collide.mp3")
goal_sound = pygame.mixer.Sound("goal.mp3")

# Window settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
RAINBOW_COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130)]
rainbow_index = 0

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
speed_increment = 0.001

# Score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Initialize ball_color, paddle_color1, and paddle_color2
ball_color = (255, 255, 255)
# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Goal screen settings
show_goal_screen = False
goal_screen_timer = 0
celebration_sound = 1

# Function to generate a random color
def random_color():
    while True:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Avoid very dark colors (close to black)
        if sum(color) > 100:
            return color

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if show_goal_screen:
        if celebration_sound == 1:
            # Play the goal sound
            goal_sound.play()  # Play the goal sound effect
            celebration_sound = 0
        # Display "GOAL" screen for 2 seconds
        if goal_screen_timer < 120:  # 2 seconds (60 frames per second)
            goal_screen_timer += 1
        else:
            show_goal_screen = False
            goal_screen_timer = 0
            # Reset the ball and continue the game
            ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)
            ball_speed_x = 2
            ball_speed_y = 2
            # Set random colors for ball and paddles after a goal
            rainbow_index = 0  # Reset the rainbow index
            ball_color = random_color()
            celebration_sound = 1

    else:
        keys = pygame.key.get_pressed()
        # Control player 1 with keyboard
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= 5
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += 5

        # Control player 2 with mouse
        mouse_pos = pygame.mouse.get_pos()
        paddle2.y = mouse_pos[1] - PADDLE_HEIGHT // 2

        # Ensure that the paddle2 doesn't go beyond the window boundaries
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > HEIGHT:
            paddle2.bottom = HEIGHT

        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collisions with paddles
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x *= -1
            # Play the collide sound
            collide_sound.play()  # Play the collision sound effect

        # Collisions with the window edges
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
            # Play the collide sound
            collide_sound.play()  # Play the collision sound effect
            
        # Score handling
        if ball.left <= 0:
            score2 += 1
            show_goal_screen = True  # Show "GOAL" screen
        elif ball.right >= WIDTH:
            score1 += 1
            show_goal_screen = True  # Show "GOAL" screen

        # Gradually increase ball speed
        ball_speed_x += speed_increment
        ball_speed_y += speed_increment

    # Limit the frame rate to 60 frames per second using clock.tick(60)
    clock.tick(60)

    # Draw on the screen
    win.fill((0, 0, 0))
    pygame.draw.rect(win, ball_color, paddle1)
    pygame.draw.rect(win, ball_color, paddle2)
    pygame.draw.ellipse(win, ball_color, ball)
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    if show_goal_screen:
        # Display "GOAL" screen in the center with rainbow colors
        goal_text = font.render("* * * * * * GOAL * * * * * *", True, RAINBOW_COLORS[rainbow_index])
        win.blit(goal_text, (WIDTH // 2 - goal_text.get_width() // 2, HEIGHT // 2 - goal_text.get_height() // 2))
        # Cycle through rainbow colors
        rainbow_index = (rainbow_index + 1) % len(RAINBOW_COLORS)
        
    pygame.display.flip()
