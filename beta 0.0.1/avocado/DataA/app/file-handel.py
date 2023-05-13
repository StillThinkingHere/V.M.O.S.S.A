import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window size to match the screen resolution
screen = pygame.display.set_mode((255, 255, 255), pygame.FULLSCREEN)

# Load the Windows shutdown image
shutdown_image = pygame.image.load("App\\poping.png")

# Set the initial rotation angle and speed
angle = 0
speed = 20

# Start the animation loop
while True:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Rotate the shutdown image
    rotated_image = pygame.transform.rotate(shutdown_image, angle)
    angle += speed

    # Draw the rotated image in the center of the screen
    screen.blit(rotated_image, rotated_image.get_rect(
        center=screen.get_rect().center))

    # Update the screen
    pygame.display.flip()

    # Wait for a short time to control the animation speed
    pygame.time.wait(50)
