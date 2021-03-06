import pygame

from settings import TILESIZE, WORLD_MAP
from camera import YSortCameraGroup
from tile import Tile
from player import Player


class Level:
	def __init__(self):
		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.player: Player = Player(self, (0, 0), (self.visible_sprites,))
		self.create_map()

	def create_map(self):
		for y_index, row in enumerate(WORLD_MAP):
			for x_index, col in enumerate(row):
				x = x_index * TILESIZE
				y = y_index * TILESIZE
				if col == 'x':
					Tile(self, (x, y), (self.visible_sprites, self.obstacle_sprites))
				if col == 'p':
					self.player.rect.topleft = x, y

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
