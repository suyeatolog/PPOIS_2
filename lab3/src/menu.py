import pygame
import random

class Button:
    def __init__(self, x, y, w, h, text, font_size=32, base_color=(50, 100, 150), hover_color=(80, 140, 190)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.freetype.Font(None, font_size)
        self.base_color = base_color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen, text_color=(255, 255, 255)):
        color = self.hover_color if self.is_hovered else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        text_rect = self.font.get_rect(self.text)
        text_rect.center = self.rect.center
        self.font.render_to(screen, text_rect, self.text, text_color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class MainMenu:
    def __init__(self, screen, config):
        self.screen = screen
        self.font = pygame.freetype.Font(None, 40)
        self.buttons = [
            Button(550, 200, 300, 60, "Играть"),
            Button(550, 280, 300, 60, "Таблица лидеров"),
            Button(550, 360, 300, 60, "Настройки"),
            Button(550, 440, 300, 60, "Справка"),
            Button(550, 520, 300, 60, "Выход")
        ]
        screen_w = config.get('screen', {}).get('width', 1400)
        screen_h = config.get('screen', {}).get('height', 800)
        self.stars = [(random.randint(0, screen_w), random.randint(0, screen_h), random.randint(1, 2))
                      for _ in range(150)]

    def draw(self, text_color=(255, 255, 255)):
        for x, y, size in self.stars:
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), size)

        self.font.render_to(self.screen, (580, 100), "PONG GAME", text_color)
        for btn in self.buttons:
            btn.draw(self.screen)

    def handle_event(self, event):
        for btn in self.buttons:
            if btn.handle_event(event):
                return btn.text.lower()
        return None

class ModeMenu:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        self.font = pygame.freetype.Font(None, 40)
        self.buttons = [
            Button(550, 300, 300, 60, "Игра с ботом"),
            Button(550, 400, 300, 60, "Игра 1 на 1")
        ]
        screen_w = config.get('screen', {}).get('width', 1400)
        screen_h = config.get('screen', {}).get('height', 800)
        self.stars = [(random.randint(0, screen_w), random.randint(0, screen_h), random.randint(1, 2)) for _ in range(150)]

    def draw(self, text_color=(255, 255, 255)):
        for x, y, size in self.stars:
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), size)
        self.font.render_to(self.screen, (540, 200), "Выберите режим", text_color)
        for btn in self.buttons:
            btn.draw(self.screen)

    def handle_event(self, event):
        for btn in self.buttons:
            if btn.handle_event(event):
                return btn.text.lower()
        return None

class Slider:
    def __init__(self, x, y, width, height, min_val=0, max_val=100, current_val=50, label=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.knob_size = height
        self.knob_rect = pygame.Rect(x, y, self.knob_size, self.knob_size)
        self.min_val = min_val
        self.max_val = max_val
        self.value = float(current_val)
        self.label = label
        self.is_dragging = False
        self.font = pygame.freetype.Font(None, 26)
        self._update_knob_pos()

    def _update_knob_pos(self):
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        self.knob_rect.x = self.rect.x + int(ratio * (self.rect.width - self.knob_size))
        self.knob_rect.y = self.rect.y

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.knob_rect.collidepoint(event.pos) or self.rect.collidepoint(event.pos):
                self.is_dragging = True
                self._update_from_mouse(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            self._update_from_mouse(event.pos)

    def _update_from_mouse(self, pos):
        rel_x = max(self.rect.x, min(pos[0], self.rect.x + self.rect.width - self.knob_size))
        ratio = (rel_x - self.rect.x) / (self.rect.width - self.knob_size)
        self.value = self.min_val + ratio * (self.max_val - self.min_val)
        self._update_knob_pos()

    def draw(self, screen):
        pygame.draw.rect(screen, (40, 40, 40), self.rect, border_radius=4)
        fill_width = int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
        pygame.draw.rect(screen, (50, 100, 150), pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height), border_radius=4)

        pygame.draw.rect(screen, (240, 240, 240), self.knob_rect, border_radius=4)

        self.font.render_to(screen, (self.rect.x, self.rect.y - 30), self.label, (255, 255, 255))
        self.font.render_to(screen, (self.rect.right + 15, self.rect.y + 2), f"{int(self.value)}%", (200, 200, 200))