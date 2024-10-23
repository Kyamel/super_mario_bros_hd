
import pyray as rl  # type: ignore
from abc import abstractmethod
from typing import List
from src.TextureManeger import TextureManager
from src.Constants import *
from src.ecs.ecs import Entity, System, World

class RenderSystem(System):
    def __init__(self, game_resolution_width: int, game_resolution_height: int) -> None:
        self.r = SKY_RED
        self.g = SKY_GREEN
        self.b = SKY_BLUE

        self.GAME_RESOLUTION_WIDTH = game_resolution_width
        self.GAME_RESOLUTION_HEIGHT = game_resolution_height

        if not rl.is_window_ready():  # Verifica se a janela já foi inicializada
            raise RuntimeError("A janela não está inicializada. Inicialize a janela antes de criar o RenderSystem.")
        rl.set_target_fps(60)  # Define a taxa de quadros por segundo

        # Inicializa o gerenciador de texturas
        self.texture_manager = TextureManager()

        rl.rl_set_blend_mode(rl.BLEND_ALPHA)


    def on_added_to_world(self, world: World) -> None:
        pass

    def set_background_color(self, r: int, g: int, b: int) -> None:
        pass

    @abstractmethod
    def tick(self, world: World) -> None:
        pass

    def on_removed_from_world(self, world: World) -> None:
        return super().on_removed_from_world(world)

    def _render_entity(self, entity: Entity, follow_camera: bool = True) -> None:
        pass

    def _render_text(self, entities: List[Entity]) -> None:
        pass