import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 900, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Set up font
FONT = pygame.font.SysFont('comicsans', 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
number_to_guess = random.randint(1, 100)
number_of_guesses = 0
guess = None
input_text = ''
message = "Guess a number between 1 and 100"
message_color = BLACK


# Function to render text
def render_text(text, color, y):
    label = FONT.render(text, 1, color)
    win.blit(label, (WIDTH // 2 - label.get_width() // 2, y))


# Game loop
running = True
while running:
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_text)
                    number_of_guesses += 1
                    if guess < number_to_guess:
                        message = "Too low! Try again."
                        message_color = RED
                    elif guess > number_to_guess:
                        message = "Too high! Try again."
                        message_color = RED
                    else:
                        message = f"Congratulations! You guessed the correct number in {number_of_guesses} guesses."
                        message_color = GREEN
                except ValueError:
                    message = "Please enter a valid number."
                    message_color = RED
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Render input box and message
    input_box = FONT.render(input_text, 1, BLACK)
    win.blit(input_box, (WIDTH // 2 - input_box.get_width() // 2, HEIGHT // 2))
    render_text(message, message_color, HEIGHT // 2 + 50)

    # Update display
    pygame.display.update()

pygame.quit()
