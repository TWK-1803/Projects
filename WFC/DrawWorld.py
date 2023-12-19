import pygame
from Config import *


class DrawWorld:

    def __init__(self, world):
        self.font0 = pygame.font.Font(pygame.font.get_default_font(), 14)
        self.font1 = pygame.font.Font(pygame.font.get_default_font(), 11)
        self.font2 = pygame.font.Font(pygame.font.get_default_font(), 8)
        self.spritesheet = pygame.image.load(SPRITESHEET_PATH).convert_alpha()
        self.world = world
        self.worldSurface = pygame.Surface((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))

    # Try/Except block is for restarting the simulation should a contradition be reached
    # Could be used for backtracking as well, but this is the simplest method of contradiction handling
    def update(self):
        lowest_entropy = self.world.getLowestEntropy()
        try:
            for y in range(WORLD_Y):
                for x in range(WORLD_X):
                    tile_entropy = self.world.getEntropy(x, y)
                    tile_type = self.world.getType(x, y)
                    if tile_entropy > 0:
                        tile_image = pygame.Surface((TILESIZE, TILESIZE))
                        if tile_entropy >= 27:
                            textSurface = self.font2.render(str(tile_entropy), True, "darkgrey")
                            tile_image.blit(textSurface, (3, 3))
                        elif tile_entropy >= 10:
                            textSurface = self.font1.render(str(tile_entropy), True, "grey")
                            tile_image.blit(textSurface, (2, 3))
                        elif tile_entropy < 10:
                            if tile_entropy == lowest_entropy:
                                textSurface = self.font0.render(str(tile_entropy), True, "green")
                            else:
                                textSurface = self.font0.render(str(tile_entropy), True, "white")
                            tile_image.blit(textSurface, (4, 1))
                    else:
                        pos = tileSprites[tile_type]
                        tile_image = self.spritesheet.subsurface(pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE))
                    tile_image = pygame.transform.scale_by(tile_image, (SCALETILE, SCALETILE))
                    self.worldSurface.blit(tile_image, (x * TILESIZE * SCALETILE, y * TILESIZE * SCALETILE))
        except:
            self.world.reset()
            self.update()

    def draw(self, displaySurface):
        displaySurface.blit(self.worldSurface, (0, 0))