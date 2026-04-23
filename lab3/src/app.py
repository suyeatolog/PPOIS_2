import os
import pygame
import sys
from config import Config
from menu import MainMenu, Slider, ModeMenu
from game import Game
from scoreboard import Scoreboard

class App:
    def __init__(self):
        pygame.init()
        self.config = Config('data/config.json')
        screen_cfg = self.config.get('screen', {'width': 1400, 'height': 800})
        self.screen = pygame.display.set_mode((screen_cfg['width'], screen_cfg['height']))
        pygame.display.set_caption('Pong Game')
        self.clock = pygame.time.Clock()
        
        self.scoreboard = Scoreboard(self.config.get('paths', {}).get('leaderboard', 'data/leaderboard.json'))
        self.state = 'menu'
        self.menu = MainMenu(self.screen, self.config)
        self.mode_menu = ModeMenu(self.screen, self.config)
        self.game_mode = 'bot'
        self.game = None
        self.results_shown = False
        self.player_score = 0
        self.player_final_score = 0
        self.running = True
        self.input_text = ""
        self.music_slider = Slider(450, 250, 400, 20, 0, 100, 50, "Громкость музыки")
        self.sfx_slider = Slider(450, 350, 400, 20, 0, 100, 50, "Громкость звуков")
        pygame.mixer.music.set_volume(0.5)

        self.current_music = None
        self.sfx_hit = None
        self.sfx_goal = None
        self._init_audio()

        pygame.mixer.init()

    def _init_audio(self):
        pygame.mixer.init()
        audio = self.config.get('audio', {})
        try:
            self.sfx_hit = pygame.mixer.Sound(audio.get('sfx_hit'))
            self.sfx_goal = pygame.mixer.Sound(audio.get('sfx_goal'))
            self._switch_music('menu')
        except Exception as e:
            print(f"Audio warning: {e}")

    def _switch_music(self, track):
        if self.current_music == track:
            return
        self.current_music = track
        path = self.config.get('audio', {}).get(f'music_{track}')
        if path and os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)

    def run(self):
        while self.running:
            self._process_events()
            self._update()
            self._draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if self.state == 'menu':
                action = self.menu.handle_event(event)
                if action == 'играть':
                    self.state = 'mode_selection'
                elif action == 'таблица лидеров':
                    self.state = 'leaderboard'
                elif action == 'настройки':
                    self.state = 'settings'
                elif action == 'справка':
                    self.state = 'help'
                elif action == 'выход':
                    self.running = False

            elif self.state == 'mode_selection':
                action = self.mode_menu.handle_event(event)
                if action == 'игра с ботом':
                    self.game_mode = 'bot'
                    self.game = Game(self.screen, self.config, self.sfx_hit, self.sfx_goal, mode='bot')
                    self._switch_music('game')
                    self.state = 'game'
                elif action == 'игра 1 на 1':
                    self.game_mode = '1v1'
                    self.game = Game(self.screen, self.config, self.sfx_hit, self.sfx_goal, mode='1v1')
                    self._switch_music('game')
                    self.state = 'game'
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = 'menu'

            elif self.state == 'game':
                self.game.handle_input(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = 'menu'

            elif self.state == 'settings':
                self.music_slider.handle_event(event)
                self.sfx_slider.handle_event(event)

                pygame.mixer.music.set_volume(self.music_slider.value / 100.0)
                if self.sfx_hit: self.sfx_hit.set_volume(self.sfx_slider.value / 100.0)
                if self.sfx_goal: self.sfx_goal.set_volume(self.sfx_slider.value / 100.0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = 'menu'

            elif self.state == 'results':
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_KP_ENTER):
                        if self.scoreboard.is_high_score(self.player_score):
                            self.state = 'dialog'
                            self.input_text = ""
                        else:
                            self.state = 'menu'
                            self._switch_music('menu')

            elif self.state == 'dialog':
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        self.scoreboard.add_score(self.input_text or "Player", self.player_score)
                        self.input_text = ""
                        self.state = 'menu'
                        self._switch_music('menu')
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode

            elif self.state in ('leaderboard', 'help', 'settings'):
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = 'menu'

    def _update(self):
        if self.state == 'game' and self.game:
            result = self.game.update()
            if result == 'finished':
                self.player_score = self.game.score[0]
                self.state = 'results'

    def _draw(self):
        self.screen.fill(self.config.get('colors', {}).get('bg', (0,0,0)))
        if self.state == 'menu':
            self.menu.draw()
        elif self.state == 'mode_selection':
            self.mode_menu.draw()
        elif self.state == 'game':
            self.game.draw()
        elif self.state == 'dialog':
            self._draw_high_score_dialog()
        elif self.state == 'leaderboard':
            self._draw_leaderboard()
        elif self.state == 'help':
            self._draw_help()
        elif self.state == 'settings':
            self._draw_settings()
        elif self.state == 'results':
            self._draw_results()
        pygame.display.flip()

    def _draw_high_score_dialog(self):
        font = pygame.freetype.Font(None, 36)
        font.render_to(self.screen, (450, 300), "Поздравляем! Новый рекорд!", (255, 215, 0))
        font.render_to(self.screen, (450, 380), f"Введите имя: {self.input_text}", (255,255,255))
        font.render_to(self.screen, (450, 700), "Нажмите Enter для сохранения", (200,200,200))

    def _draw_leaderboard(self):
        font = pygame.freetype.Font(None, 36)
        font.render_to(self.screen, (560, 80), "Таблица лидеров:", (255, 215, 0))

        top = self.scoreboard.get_top()
        if not top:
            font.render_to(self.screen, (500, 380), "Пока нет рекордов", (200, 200, 200))
        else:
            for i, entry in enumerate(top, 1):
                color = (255, 215, 0) if i == 1 else (255, 255, 255)
                line = f"{i}. {entry['name']} — {entry['score']} голов"
                font.render_to(self.screen, (480, 140 + i * 40), line, color)

        font.render_to(self.screen, (500, 700), "Нажмите ESC для возврата", (200, 200, 200))

    def _draw_help(self):
        font = pygame.freetype.Font(None, 28)
        font.render_to(self.screen, (400, 200), "Правила игры Pong:", (255, 255, 255))
        font.render_to(self.screen, (400, 250), "- Управление: W / S", (255, 255, 255))
        font.render_to(self.screen, (400, 300), "- Забейте как можно больше голов!", (255, 255, 255))
        font.render_to(self.screen, (400, 350), "- Рекорд сохраняется по количеству ваших голов", (255, 255, 255))
        font.render_to(self.screen, (500, 700), "Нажмите ESC для возврата", (200, 200, 200))

    def _draw_settings(self):
        font = pygame.freetype.Font(None, 36)
        font.render_to(self.screen, (560, 100), "Настройки звука", (255, 255, 255))

        self.music_slider.draw(self.screen)
        self.sfx_slider.draw(self.screen)

        font.render_to(self.screen, (300, 700), "Нажмите ESC для возврата и сохранения настроек", (200, 200, 200))

    def _draw_results(self):
        overlay = pygame.Surface((1400, 800), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        font_large = pygame.freetype.Font(None, 50)
        font_medium = pygame.freetype.Font(None, 36)

        font_large.render_to(self.screen, (560, 200), "Время вышло!", (255, 215, 0))

        score_text = f"Ваш счёт: {self.player_score}"
        bot_score = self.game.score[1] if self.game else 0
        result_text = f"Итог: {self.player_score} : {bot_score}"

        font_medium.render_to(self.screen, (560, 350), score_text, (255, 255, 255))
        font_medium.render_to(self.screen, (560, 400), result_text, (200, 200, 200))

        hint = "Нажмите [SPACE] или [ENTER] для продолжения"
        font_medium.render_to(self.screen, (300, 700), hint, (150, 150, 150))