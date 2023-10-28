import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 60

# Create a font for the title
title_font = pygame.font.Font(None, 72)

# Create a font for buttons
button_font = pygame.font.Font(None, 36)

# Define button coordinates
easy_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 - 80, BUTTON_WIDTH, BUTTON_HEIGHT)
medium_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
hard_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 + 80, BUTTON_WIDTH, BUTTON_HEIGHT)

# Exit button settings
exit_button_rect = pygame.Rect(WIDTH - 120, HEIGHT - 60, 100, 40)
exit_button_text = button_font.render("Exit", True, BLACK)

# Function to check if the mouse is over a button
def is_mouse_over_button(button_rect):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return button_rect.collidepoint(mouse_x, mouse_y)

# Main game loop
selected_difficulty = None
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Clear the screen
    win.fill((0, 0, 0))
    # Check if the mouse is over the easy button
    if is_mouse_over_button(easy_button_rect):
        pygame.draw.rect(win, GRAY, easy_button_rect)  # Gray background
        easy_button_label = button_font.render("Easy", True, WHITE)
    else:
        pygame.draw.rect(win, WHITE, easy_button_rect)  # Revert to white background
        easy_button_label = button_font.render("Easy", True, BLACK)

    # Check if the mouse is over the medium button
    if is_mouse_over_button(medium_button_rect):
        pygame.draw.rect(win, GRAY, medium_button_rect)  # Gray background
        medium_button_label = button_font.render("Medium", True, WHITE)
    else:
        pygame.draw.rect(win, WHITE, medium_button_rect)  # Revert to white background
        medium_button_label = button_font.render("Medium", True, BLACK)

    # Check if the mouse is over the hard button
    if is_mouse_over_button(hard_button_rect):
        pygame.draw.rect(win, GRAY, hard_button_rect)  # Gray background
        hard_button_label = button_font.render("Hard", True, WHITE)
    else:
        pygame.draw.rect(win, WHITE, hard_button_rect)  # Revert to white background
        hard_button_label = button_font.render("Hard", True, BLACK)

    # Check if the mouse is over the exit button
    if is_mouse_over_button(exit_button_rect):
        pygame.draw.rect(win, GRAY, exit_button_rect)  # Gray background
        exit_button_label = button_font.render("Exit", True, WHITE)  # Corrected color to WHITE
    else:
        pygame.draw.rect(win, WHITE, exit_button_rect)  # Revert to white background
        exit_button_label = button_font.render("Exit", True, BLACK)  # Corrected color to BLACK

    # Draw the title text (PONG)
    title_text = title_font.render("- PONG -", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, 80)
    win.blit(title_text, title_rect)

    # Calculate text positions to center them on the buttons
    easy_label_rect = easy_button_label.get_rect(center=easy_button_rect.center)
    medium_label_rect = medium_button_label.get_rect(center=medium_button_rect.center)
    hard_label_rect = hard_button_label.get_rect(center=hard_button_rect.center)

    # Draw the button labels with centered text
    win.blit(easy_button_label, easy_label_rect)
    win.blit(medium_button_label, medium_label_rect)
    win.blit(hard_button_label, hard_label_rect)
    
    # Draw the exit button with text
    exit_label_rect = exit_button_label.get_rect(center=exit_button_rect.center)
    win.blit(exit_button_label, exit_label_rect)

    # Update the display
    pygame.display.update()

    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            if is_mouse_over_button(easy_button_rect):
                selected_difficulty = "easy"
            elif is_mouse_over_button(medium_button_rect):
                selected_difficulty = "medium"
            elif is_mouse_over_button(hard_button_rect):
                selected_difficulty = "hard"
            elif is_mouse_over_button(exit_button_rect):
                running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Start the game with the selected difficulty
    if selected_difficulty:
        from game import play_pong_game
        play_pong_game(selected_difficulty)
        selected_difficulty = None

# Quit pygame properly
pygame.quit()
sys.exit()
