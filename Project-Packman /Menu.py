import pygame
import sys

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 58)

        self.score = 0
        self.high_score = 0

        #przyciski
        self.start_button_rect = pygame.Rect(self.width // 2 - 150, 300, 300, 60)
        self.quit_button_rect = pygame.Rect(self.width // 2 - 150, 400, 300, 60)

    def draw(self):
        """rysowanie wszystkich elementów menu"""
        self.screen.fill(pygame.Color('blue4'))

        #tytuł
        title_text = self.large_font.render("Pacman Game", True, pygame.Color('yellow'))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 100))

        #wyniki
        score_text = self.font.render(f"Score: {self.score}", True, pygame.Color('white'))
        self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, 150))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, pygame.Color('white'))
        self.screen.blit(high_score_text, (self.width // 2 - high_score_text.get_width() // 2, 200))

        #rysowanie przycisków
        self.draw_button(1, self.start_button_rect, "Start Game", pygame.Color('chartreuse4'), pygame.Color('white'))
        self.draw_button(2, self.quit_button_rect, "Quit Game", pygame.Color('red'), pygame.Color('white'))

        pygame.display.update()

    def draw_button(self, id, rect, text, color, text_color):
        """rysowanie pojedynczego przycisku"""
        mouse_pos = pygame.mouse.get_pos() #pobieranie pozycji myszy
        if rect.collidepoint(mouse_pos):
            if id == 1:
                color = pygame.Color('darkgreen')
            if id == 2:
                color = pygame.Color('darkred')
        pygame.draw.rect(self.screen, color, rect, border_radius=10)

        # Rysowanie tekstu w przycisku
        button_text = self.font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=rect.center) #dopasowanie tekstu do środka przycisku
        self.screen.blit(button_text, text_rect)


    def update_score(self, score):
        """Zaktualizuj wynik i sprawdź, czy jest wyższy niż dotychczasowy rekord"""
        if score > self.high_score:
            self.high_score = score
        self.score = score

    def handle_input(self):
        """
        Obsługuje wejście z myszy i klawiatury
        :return "start_game" - rozpoczęcie gierki, "menu" - nic nie robi (pozostajemy w menu)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "start_game"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.start_button_rect.collidepoint(mouse_pos):
                    return "start_game"
                elif self.quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        return "menu"

