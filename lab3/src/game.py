import pygame
from entities import Paddle, Ball


class Game:
    def __init__(self, screen, config, sfx_hit=None, sfx_goal=None, mode='bot'):
        self.screen = screen
        self.cfg = config.get('game', {})
        self.colors = config.get('colors', {})
        self.sfx_hit = sfx_hit
        self.sfx_goal = sfx_goal
        self.mode = mode

        self.player = Paddle(10, 350, 15, 100, self.colors['player'], 6)
        self.right_paddle = Paddle(1375, 350, 15, 100, self.colors['bot'], self.cfg['bot_speed'])
        self.ball = Ball(695, 395, 10, 10, self.colors['ball'])
        self.ball.reset(-1)

        self.score = [0, 0]
        self.font = pygame.freetype.Font(None, 30)
        self.running = True

        self.ball_hit_count = 0
        self.speed_up_count = 0

        self.round_time = config.get('game', {}).get('round_time', 45)
        self.start_ticks = pygame.time.get_ticks()
        self.time_left = self.round_time

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: self.player.vel_y = -self.player.speed
            if event.key == pygame.K_s: self.player.vel_y = self.player.speed

            if self.mode == '1v1':
                if event.key == pygame.K_UP: self.right_paddle.vel_y = -self.right_paddle.speed
                if event.key == pygame.K_DOWN: self.right_paddle.vel_y = self.right_paddle.speed

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s): self.player.vel_y = 0
            if self.mode == '1v1' and event.key in (pygame.K_UP, pygame.K_DOWN):
                self.right_paddle.vel_y = 0

    def update(self):
        if not self.running: return 'finished'

        elapsed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = max(0, self.round_time - elapsed)

        if self.mode == 'bot':
            self._update_bot_ai()

        self.player.move()
        self.right_paddle.move()
        self.ball.move()

        if self.ball.top <= 0 or self.ball.bottom >= 800:
            if self.sfx_hit: self.sfx_hit.play()

        self._handle_collisions()

        if self.ball.right < 0:
            if self.sfx_goal: self.sfx_goal.play()
            self.score[1] += 1
            self._reset_round(-1)
        elif self.ball.left > 1400:
            if self.sfx_goal: self.sfx_goal.play()
            self.score[0] += 1
            self._reset_round(1)

        if self.time_left <= 0:
            self.running = False
            return 'finished'

        return 'playing'

    def _update_bot_ai(self):
        if self.ball.centerx >= 400 and self.ball.speed_x > 0:
            if self.ball.centery > self.right_paddle.centery:
                self.right_paddle.vel_y = self.right_paddle.speed
            elif self.ball.centery < self.right_paddle.centery:
                self.right_paddle.vel_y = -self.right_paddle.speed
            else:
                self.right_paddle.vel_y = 0
        else:
            self.right_paddle.vel_y = 0

    def _handle_collisions(self):
        if self.ball.colliderect(self.right_paddle):
            if self.sfx_hit: self.sfx_hit.play()
            self.ball.speed_x = -self.ball.speed_x - 1
            self.ball_hit_count += 1
            if self.ball_hit_count == 2:
                if self.ball.speed_y < 0: self.ball.speed_y -= 1
                else: self.ball.speed_y += 1
                self.ball_hit_count = 0

        if self.ball.colliderect(self.player):
            if self.sfx_hit: self.sfx_hit.play()
            self.ball.speed_x = -self.ball.speed_x + 1
            self.ball_hit_count += 1
            if self.ball_hit_count == 2:
                if self.ball.speed_y < 0: self.ball.speed_y -= 1
                else: self.ball.speed_y += 1
                self.ball_hit_count = 0

    def _reset_round(self, direction):
        self.ball.reset(direction)
        self.right_paddle.speed = self.cfg.get('bot_speed', 5)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (5, 5, 1390, 790), 3)
        for y in range(0, 800, 30):
            pygame.draw.line(self.screen, (255, 255, 255), (700, y), (700, y + 15), 2)

        self.font.render_to(self.screen, (680, 20), f"{self.score[0]}:{self.score[1]}", self.colors['text'])
        self.font.render_to(self.screen, (650, 50), f"Time: {int(self.time_left)}s", self.colors['text'])

        self.player.draw(self.screen)
        self.right_paddle.draw(self.screen)
        self.ball.draw(self.screen)