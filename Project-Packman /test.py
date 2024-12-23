import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Wymiary ekranu
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCORE_HEIGHT = 100  # Wysokość pola na wynik

# Kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Czcionka
FONT_SIZE = 30
font = pygame.font.Font(None, FONT_SIZE)

# Tworzenie ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gra Pac-Man")

# Wynik
score = 0

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logika gry (np. aktualizacja wyniku)
    # score += 1  # Możesz modyfikować wynik w zależności od rozgrywki

    # Rysowanie ekranu
    screen.fill(BLACK)  # Czyszczenie ekranu

    # Rysowanie pola wyniku
    pygame.draw.rect(screen, BLUE, (0, 0, SCREEN_WIDTH, SCORE_HEIGHT))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))  # Wyświetlanie wyniku

    # Rysowanie pola gry
    pygame.draw.rect(screen, WHITE, (0, SCORE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - SCORE_HEIGHT), 1)

    # Odświeżanie ekranu
    pygame.display.flip()

# Zakończenie gry
pygame.quit()
sys.exit()
