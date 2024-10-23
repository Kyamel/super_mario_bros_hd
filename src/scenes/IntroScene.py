import raylib as rl # type: ignore
from src.Constants import *
from src.scenes.Scene import Scene
from src.systems.RenderSystem import RenderSystem

class IntroScene(Scene):
    def __init__(self):
        super().__init__()
        self.timer = 0

        self.world.register_system(RenderSystem)

    def is_finished(self):
        return self.timer >= INTRO_SCREEN_TIME

    def update(self):
        self.timer += 1
        super().update()

