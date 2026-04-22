import pygame
from entities import Paddle, Ball

class Game:
    def __init__(self, screen, config, sfx_hit=None, sfx_goal=None):
        self.screen = screen
        self.cfg = config.get('game', {})
        self.colors = config.get('colors', {})
        self.sfx_hit = sfx_hit
        self.sfx_goal = sfx_goal
        
        self.player = Paddle(10, 350, 15, 100, self.colors['player'], 6)
        self.bot = Paddle(1375, 350, 15, 100, self.colors['bot'], self.cfg['bot_speed'])
        self.ball = Ball(695, 395, 10, 10, self.colors['ball'])
        self.ball.reset(-1)
        
        self.score = [0, 0]
        self.font = pygame.freetype.Font(None, 30)
        self.running = True
        self.bot_speed_counter = 0
        # self.max_score = self.cfg.get('max_score', 3)
        self.round_time = config.get('game', {}).get('round_time', 45)
        self.start_ticks = pygame.time.get_ticks()  # Старт таймера
        self.time_left = self.round_time

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                self.player.vel_y = -self.player.speed
            if event.key == pygame.K_s: 
                self.player.vel_y = self.player.speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s): 
                self.player.vel_y = 0

    def update(self):
        if not self.running:
            return 'finished'

        elapsed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = max(0, self.round_time - elapsed)

        self.player.move()
        self.ball.move()

        if self.ball.top <= 0 or self.ball.bottom >= 800:
            if self.sfx_hit: self.sfx_hit.play()

        self._handle_collisions()
        self._control_bot()

        if self.ball.right < 0:
            if self.sfx_goal: self.sfx_goal.play()
            self.score[1] += 1
            self.ball.reset(-1)
        elif self.ball.left > 1400:
            if self.sfx_goal: self.sfx_goal.play()
            self.score[0] += 1
            self.ball.reset(1)

        if self.time_left <= 0:
            self.running = False
            return 'finished'

        return 'playing'

    def _handle_collisions(self):
        if self.ball.colliderect(self.bot):
            if self.sfx_hit: self.sfx_hit.play()
            self.ball.speed_x = -self.ball.speed_x - 1
            self.ball.hit_counter += 1
            if self.ball.hit_counter == 2:
                if self.ball.speed_y < 0: 
                    self.ball.speed_y -= 1
                if self.ball.speed_y > 0:
                    self.ball.speed_y += 1
                self.ball.hit_counter = 0
            self.bot_speed_counter += 1
            if self.bot_speed_counter == 4:
                self.bot_speed_counter = 0
                self.bot.speed += 1

        if self.ball.colliderect(self.player):
            if self.sfx_hit: self.sfx_hit.play()
            self.ball.speed_x = -self.ball.speed_x + 1
            self.ball.hit_counter += 1
            if self.ball.hit_counter == 2:
                if self.ball.speed_y < 0: 
                    self.ball.speed_y -= 1
                if self.ball.speed_y > 0: 
                    self.ball.speed_y += 1
                self.ball.hit_counter = 0
            self.bot_speed_counter += 1
            if self.bot_speed_counter == 4:
                self.bot_speed_counter = 0
                self.bot.speed += 1

    def _control_bot(self):
        if self.ball.centerx >= 400 and self.ball.speed_x > 0:
            if self.ball.centery > self.bot.centery:
                self.bot.move(1)
            elif self.ball.centery < self.bot.centery:
                self.bot.move(-1)

    def _reset_round(self, direction):
        self.ball.reset(direction)
        self.bot.reset()
        self.bot.speed = 5.5

    def draw(self):
        self.font.render_to(self.screen, (680, 20), f"{self.score[0]}:{self.score[1]}", self.colors['text'])

        timer_text = f"Time: {int(self.time_left)}s"
        self.font.render_to(self.screen, (650, 50), timer_text, self.colors['text'])

        self.player.draw(self.screen)
        self.bot.draw(self.screen)
        self.ball.draw(self.screen)