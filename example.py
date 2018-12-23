import pygame
import blocks

class LevelOne(blocks.Stage):
    def __init__(self):
        blocks.Stage.__init__(self, 40)

        tree_ground = blocks.Tile(blocks.Color('lawngreen').darken(0.8), flat=True)
        self.images = [
            blocks.Block(blocks.Color('lawngreen')),
            blocks.Block(blocks.Color('firebrick')),
            blocks.Tile(blocks.Color('lawngreen')),
            blocks.Tile(blocks.Color('lawngreen'), flat=True),
            blocks.Brick(blocks.Color('gray40'), blocks.Color('firebrick'), flat=True),
            blocks.Brick(blocks.Color('gray40'), blocks.Color('firebrick')),
            blocks.Crate(blocks.Color('burlywood3')),
            blocks.IceBlock(blocks.Color('cyan2')),
            blocks.Tree(blocks.Color('forestgreen'), blocks.Color('brown'), tree_ground),
            blocks.IceBlock(blocks.Color('skyblue')),
        ]

        #self.map_area(range(10, 12), range(16, 24), (0, 2))
        self.map_area(range(12, 14), range(16, 24), (0, 4))
        self.map_range_row(range(11, 14), 11, (0, 2))
        self.map_range_row(range(16, 19), 11, (0, 7))
        self.map_range_row(range(16, 24), 14, (0, 3))
        self.map_range_row(range(18, 24), 16, (0, 5))
        self.map_range_row(range(18, 22), 17, (0, 6))
        self.map_range_col(range(7, 12), 23, (0, 0))
        self.map_range_col(range(14, 16), 12, (0, 9))
        self.map_add(14, 17, ((0, 8),))
        self.map_add(14, 22, ((0, 8),))
        # HI
        self.map_stack_range(range(5), 9, 23, 0)
        self.map_stack_range(range(5), 9, 20, 0)
        self.map_range_row(range(21, 23), 9, (2, 0))
        self.map_stack_range(range(5), 9, 17, 1)
        self.map_stack_range((0, 4), 9, 16, 1)
        self.map_stack_range((0, 4), 9, 18, 1)
        # end HI

class Scene:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 800, 600)
        pygame.display.set_caption('Example')
        self.surface = pygame.display.set_mode(self.rect.size)
        self.clock = pygame.time.Clock()

        self.stage = LevelOne()
        self.stage.setup_draw(self.surface)
        self.pos = (13, 19)

    def loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill((0,0,0))

            self.stage.draw(self.surface, self.pos)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

scene = Scene()
scene.loop()
