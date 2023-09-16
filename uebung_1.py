import os
import random
import pygame

def random_obstacle_position_x() -> int:
    return random.randint(75, Settings.WINDOW.width - Settings.OBSTACLE_SIZE)

def random_obstacle_position_y() -> int:
    return random.randint(75, Settings.WINDOW.height - Settings.OBSTACLE_SIZE)

class Settings:
    WINDOW = pygame.rect.Rect(0, 0, 960, 540)
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    ASSET_PATH = os.path.join(FILE_PATH, "assets")
    IMAGE_PATH = os.path.join(FILE_PATH, ASSET_PATH, "images")
    OBSTACLE_SIZE = 50
    OBSTACLE_NUM = 5
    OBJECT_SIZE = 30
    OBJECT_SPAWNRATE = 200

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image: str, scale_multiply_x: float = 1.0, scale_multiply_y: float = 1.0) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.OBSTACLE_SIZE * scale_multiply_x, Settings.OBSTACLE_SIZE * scale_multiply_y))
        self.rect = self.image.get_rect()
        self.rect.left = random_obstacle_position_x()
        self.rect.bottom = random_obstacle_position_y()

class Test6(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "test.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.OBJECT_SIZE, Settings.OBJECT_SIZE))
        self.image.set_colorkey("black")
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.top = 10
        self.speedx = random.uniform(1.5, 5.5)
        self.speedy = random.uniform(1.5, 5.5)
    
    def update(self) -> None:
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.right > Settings.WINDOW.right or self.rect.left <= 0:
            self.speedx *= -1
        if self.rect.bottom > Settings.WINDOW.bottom or self.rect.top <= 0:
            self.speedy *= -1

class Game:
    def __init__(self) -> None:
        self.time_start = pygame.time.get_ticks()
        os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.WINDOW.size))
        pygame.display.set_caption("Bitmaps laden und ausgeben")
        self.clock = pygame.time.Clock()

        self.all_obstacles = pygame.sprite.Group()
        for _ in range(Settings.OBSTACLE_NUM):
            self.obstacles = Obstacle("test.png", random.uniform(0.75, 1.5), random.uniform(0.75, 1.5))
            self.all_obstacles.add(self.obstacles)

        self.object = Test6()
        self.all_objects = pygame.sprite.Group()
        self.all_objects.add(self.object)

        self.running = True

    def run(self) -> None:
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.spawn_new_mob()
            self.clock.tick(Settings.FPS)

    def update(self) -> None:
        self.all_objects.update()

    def spawn_new_mob(self) -> None:
        # Wie man Objekte nach einer gewissen Zeit spawnt: https://stackoverflow.com/questions/52917306/i-have-been-trying-to-have-a-new-enemy-spawn-every-20-seconds-using-pygame
        time_now = pygame.time.get_ticks()
        if time_now - self.time_start > Settings.OBJECT_SPAWNRATE:
            self.time_start = time_now            
            self.object = Test6()
            self.all_objects.add(self.object)

    def draw(self) -> None:
        self.screen.fill("black")
        self.all_obstacles.draw(self.screen)
        self.all_objects.draw(self.screen)
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