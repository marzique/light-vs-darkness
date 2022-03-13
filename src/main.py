import sys

import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF

from settings import WIDTH, HEIGTH, FPS, CAPTION
from level import Level


class Game:
	WINDOW_SETTINGS = pygame.SCALED | HWSURFACE | DOUBLEBUF  # | pygame.NOFRAME

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH), self.WINDOW_SETTINGS)
		pygame.display.set_caption(CAPTION)
		self.clock = pygame.time.Clock()
		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('#1a1a25')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == '__main__':
	game = Game()
	game.run()
