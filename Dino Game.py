import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Dino setup
dino = pygame.Rect(50, HEIGHT - 90, 40, 40)
dino_vel_y = 0
gravity = 1
is_jumping = False

# Obstacle setup
obstacle = pygame.Rect(WIDTH, HEIGHT - 90, 30, 50)
obstacle_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                dino_vel_y = -15

    # Dino movement
    if is_jumping:
        dino.y += dino_vel_y
        dino_vel_y += gravity
        if dino.y >= HEIGHT - 90:
            dino.y = HEIGHT - 90
            is_jumping = False

    # Obstacle movement
    obstacle.x -= obstacle_speed
    if obstacle.x < -30:
        obstacle.x = WIDTH
        score += 1

    # Collision detection
    if dino.colliderect(obstacle):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    pygame.draw.rect(screen, BLACK, dino)
    pygame.draw.rect(screen, BLACK, obstacle)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
