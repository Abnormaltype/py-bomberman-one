import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

from app.settings import DEFAULT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from app.weapons.bomb import Bomb


class Player(pygame.sprite.Sprite):
    def __init__(self, bomberman):
        super(Player, self).__init__()
        self.bomberman = bomberman
        self.surf = pygame.Surface((20, 40))
        self.surf = pygame.image.load(
            "images/player_front.png"
        ).convert_alpha()
        self.rect = self.surf.get_rect()
        self.is_planting = 60

    def update(self):
        self.is_planting += 1
        if self.bomberman.pressed_keys[K_UP]:
            self.rect.move_ip(0, -DEFAULT_SPEED)

            if pygame.sprite.spritecollideany(self, self.bomberman.walls):
                self.rect.move_ip(0, DEFAULT_SPEED)

            if self.bomberman.bombs and \
                    pygame.sprite.spritecollideany(self, self.bomberman.bombs):
                self.rect.move_ip(0, DEFAULT_SPEED)

            self.surf = pygame.image.load(
                "images/player_back.png"
            ).convert_alpha()

        if self.bomberman.pressed_keys[K_DOWN]:
            self.rect.move_ip(0, DEFAULT_SPEED)

            if pygame.sprite.spritecollideany(self, self.bomberman.walls):
                self.rect.move_ip(0, -DEFAULT_SPEED)

            if self.bomberman.bombs and \
                    pygame.sprite.spritecollideany(self, self.bomberman.bombs):
                self.rect.move_ip(0, -DEFAULT_SPEED)

            self.surf = pygame.image.load(
                "images/player_front.png"
            ).convert_alpha()

        if self.bomberman.pressed_keys[K_LEFT]:
            self.rect.move_ip(-DEFAULT_SPEED, 0)

            if pygame.sprite.spritecollideany(self, self.bomberman.walls):
                self.rect.move_ip(DEFAULT_SPEED, 0)

            if self.bomberman.bombs and \
                    pygame.sprite.spritecollideany(self, self.bomberman.bombs):
                self.rect.move_ip(DEFAULT_SPEED, 0)

            self.surf = pygame.image.load(
                "images/player_left.png"
            ).convert_alpha()

        if self.bomberman.pressed_keys[K_RIGHT]:
            self.rect.move_ip(DEFAULT_SPEED, 0)

            if pygame.sprite.spritecollideany(self, self.bomberman.walls):
                self.rect.move_ip(-DEFAULT_SPEED, 0)

            if self.bomberman.bombs and \
                    pygame.sprite.spritecollideany(self, self.bomberman.bombs):
                self.rect.move_ip(-DEFAULT_SPEED, 0)

            self.surf = pygame.image.load(
                "images/player_right.png"
            ).convert_alpha()

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def plant_bomb(self):
        if self.is_planting >= 60:
            self.is_planting = 0
            x, y = self.rect.x, self.rect.y
            center_bomb = Bomb((x, y)).create_centers_of_bombs((x, y))

            return Bomb(center_bomb)