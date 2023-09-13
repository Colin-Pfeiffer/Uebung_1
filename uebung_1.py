import os
import pygame


class Settings:
    WINDOW = pygame.rect.Rect(0, 0, 600, 400)
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    ASSET_PATH = os.path.join(FILE_PATH, "assets")
    IMAGE_PATH = os.path.join(FILE_PATH, ASSET_PATH, "images")

class Game:
    def __init__(self) -> None:
        os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.WINDOW.size))
        pygame.display.set_caption("Bitmaps laden und ausgeben")
        self.clock = pygame.time.Clock()

        self.running = True

    def run(self) -> None:
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(Settings.FPS)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pygame.display.flip()

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

def main():
    game = Game()
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()