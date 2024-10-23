from typing import Dict
import pyray as rl  # type: ignore
from src.Constants import TILE_SIZE
from enum import Enum

class TextureId(Enum):
    EMPTY = 0
    MARIO_STAND = 1
    MARIO_RUN_1 = 2
    MARIO_RUN_2 = 3
    MARIO_RUN_3 = 4
    MARIO_JUMP = 5
    MARIO_DRIFT = 6
    MARIO_DEAD = 7
    MARIO_GROWING = 8
    SUPER_MARIO_STAND = 9
    SUPER_MARIO_RUN_1 = 10
    SUPER_MARIO_RUN_2 = 11
    SUPER_MARIO_RUN_3 = 12
    SUPER_MARIO_JUMP = 13
    SUPER_MARIO_DRIFT = 14
    SUPER_MARIO_DUCK = 15
    GOOMBA = 16
    GOOMBA_CRUSHED = 17
    QUESTION_BLOCK_1 = 18
    QUESTION_BLOCK_2 = 19
    QUESTION_BLOCK_3 = 20
    QUESTION_BLOCK_OFF = 21
    MUSHROOM = 22
    FLOOR = 23
    TUBE_TOP_LEFT = 24
    TUBE_TOP_RIGHT = 25
    TUBE_RIGHT = 26
    TUBE_LEFT = 27
    CLOUD = 28
    BRICK = 29
    BLOCK = 30
    BUSH_RIGHT = 31
    BUSH_CENTER = 32
    BUSH_LEFT = 33
    BACKGROUND_CLOUD_TOP_LEFT = 34
    BACKGROUND_CLOUD_TOP_CENTER = 35
    BACKGROUND_CLOUD_TOP_RIGHT = 36
    BACKGROUND_CLOUD_BOTTOM_LEFT = 37
    BACKGROUND_CLOUD_BOTTOM_CENTER = 38
    BACKGROUND_CLOUD_BOTTOM_RIGHT = 39
    BRICK_DEBRIS_1 = 40
    BRICK_DEBRIS_2 = 41
    BRICK_DEBRIS_3 = 42
    BRICK_DEBRIS_4 = 43
    BACKGROUND_MOUNTAIN_1 = 44
    BACKGROUND_MOUNTAIN_2 = 45
    BACKGROUND_MOUNTAIN_3 = 46
    BACKGROUND_MOUNTAIN_4 = 47
    BACKGROUND_MOUNTAIN_5 = 48
    COIN_1 = 49
    COIN_2 = 50
    COIN_3 = 51
    COIN_4 = 52
    TURTLE_1 = 53
    TURTLE_2 = 54
    TURTLE_SHELL_1 = 55
    TURTLE_SHELL_2 = 56
    FLAG_TOP = 57
    FLAG_RIGHT = 58
    FLAG_LEFT = 59
    FLAG_POLE = 60
    CASTLE_1 = 61
    CASTLE_2 = 62
    CASTLE_3 = 63
    CASTLE_4 = 64
    CASTLE_5 = 65
    CASTLE_6 = 66
    CASTLE_DOOR = 67
    CASTLE_8 = 68
    COIN_SMALL_1 = 69
    COIN_SMALL_2 = 70
    COIN_SMALL_3 = 71
    ONE_UP = 72
    ONE_UP_LABEL = 73
    ONEHUNDRED = 74
    TWOHUNDRED = 75
    THOUSAND = 76
    MARIO_FLAG_1 = 77
    MARIO_FLAG_2 = 78

class TextureManager:
    def __init__(self) -> None:
        # Carregar a textura principal
        self.texture = rl.load_texture("assets/tileset.png")
        if not self.texture.id:
            print("[Texture manager] Unable to load texture")
            raise ValueError("Unable to load texture")

        # Inicializar o dicionário de texturas
        self.textures: Dict[TextureId, rl.Rectangle] = {}

        # Adicionar texturas do Mario
        self.textures[TextureId.MARIO_STAND] = rl.Rectangle(0, 254, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_RUN_1] = rl.Rectangle(17, 254, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_RUN_2] = rl.Rectangle(34, 254, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_RUN_3] = rl.Rectangle(51, 254, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_JUMP] = rl.Rectangle(85, 254, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_DRIFT] = rl.Rectangle(68, 254, TILE_SIZE, TILE_SIZE)

        # Adicionar texturas grandes do Mario
        self.textures[TextureId.MARIO_GROWING] = rl.Rectangle(136, 271, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_STAND] = rl.Rectangle(0, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_RUN_1] = rl.Rectangle(17, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_RUN_2] = rl.Rectangle(34, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_RUN_3] = rl.Rectangle(51, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_JUMP] = rl.Rectangle(85, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_DRIFT] = rl.Rectangle(68, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.SUPER_MARIO_DUCK] = rl.Rectangle(102, 221, TILE_SIZE, TILE_SIZE * 2)

        # Adicionar tiles
        self.textures[TextureId.FLOOR] = rl.Rectangle(0, 0, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.QUESTION_BLOCK_1] = rl.Rectangle(0, 204, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.QUESTION_BLOCK_2] = rl.Rectangle(17, 204, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.QUESTION_BLOCK_3] = rl.Rectangle(34, 204, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.QUESTION_BLOCK_OFF] = rl.Rectangle(51, 204, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MUSHROOM] = rl.Rectangle(119, 204, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.TUBE_TOP_LEFT] = rl.Rectangle(0, 34, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.TUBE_TOP_RIGHT] = rl.Rectangle(17, 34, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.TUBE_LEFT] = rl.Rectangle(0, 51, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.TUBE_RIGHT] = rl.Rectangle(17, 51, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CLOUD] = rl.Rectangle(204, 51, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.GOOMBA] = rl.Rectangle(119, 187, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.GOOMBA_CRUSHED] = rl.Rectangle(102, 187, TILE_SIZE, TILE_SIZE)

        # Definindo um dicionário para armazenar as texturas
        self.textures[TextureId.BLOCK] = rl.Rectangle(34, 34, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BRICK] = rl.Rectangle(85, 0, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BUSH_LEFT] = rl.Rectangle(34, 0, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BUSH_CENTER] = rl.Rectangle(51, 0, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BUSH_RIGHT] = rl.Rectangle(68, 0, TILE_SIZE, TILE_SIZE)

        # Background clouds
        self.textures[TextureId.BACKGROUND_CLOUD_TOP_LEFT] = rl.Rectangle(0, 119, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_CLOUD_TOP_CENTER] = rl.Rectangle(17, 119, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_CLOUD_TOP_RIGHT] = rl.Rectangle(34, 119, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_CLOUD_BOTTOM_LEFT] = rl.Rectangle(0, 136, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_CLOUD_BOTTOM_CENTER] = rl.Rectangle(17, 136, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_CLOUD_BOTTOM_RIGHT] = rl.Rectangle(34, 136, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.BRICK_DEBRIS_1] = rl.Rectangle(136, 153, 8, 8)
        self.textures[TextureId.BRICK_DEBRIS_2] = rl.Rectangle(144, 153, 8, 8)
        self.textures[TextureId.BRICK_DEBRIS_3] = rl.Rectangle(136, 161, 8, 8)
        self.textures[TextureId.BRICK_DEBRIS_4] = rl.Rectangle(144, 161, 8, 8)

        self.textures[TextureId.BACKGROUND_MOUNTAIN_1] = rl.Rectangle(0, 17, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_MOUNTAIN_2] = rl.Rectangle(17, 17, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_MOUNTAIN_3] = rl.Rectangle(34, 17, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_MOUNTAIN_4] = rl.Rectangle(17, 0, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.BACKGROUND_MOUNTAIN_5] = rl.Rectangle(51, 17, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.COIN_1] = rl.Rectangle(153, 153, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.COIN_2] = rl.Rectangle(170, 153, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.COIN_3] = rl.Rectangle(187, 153, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.COIN_4] = rl.Rectangle(204, 153, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.TURTLE_1] = rl.Rectangle(119, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.TURTLE_2] = rl.Rectangle(136, 221, TILE_SIZE, TILE_SIZE * 2)
        self.textures[TextureId.TURTLE_SHELL_1] = rl.Rectangle(153, 237, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.TURTLE_SHELL_2] = rl.Rectangle(170, 237, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.MARIO_DEAD] = rl.Rectangle(102, 254, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.FLAG_TOP] = rl.Rectangle(51, 34, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.FLAG_RIGHT] = rl.Rectangle(51, 51, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.FLAG_LEFT] = rl.Rectangle(34, 51, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.FLAG_POLE] = rl.Rectangle(187, 119, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_1] = rl.Rectangle(0, 68, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_2] = rl.Rectangle(17, 68, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_3] = rl.Rectangle(34, 68, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_4] = rl.Rectangle(0, 85, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_5] = rl.Rectangle(17, 85, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_6] = rl.Rectangle(34, 85, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_DOOR] = rl.Rectangle(17, 102, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.CASTLE_8] = rl.Rectangle(0, 102, TILE_SIZE, TILE_SIZE)


        self.textures[TextureId.COIN_SMALL_1] = rl.Rectangle(119, 254, 5, 8)
        self.textures[TextureId.COIN_SMALL_2] = rl.Rectangle(129, 254, 5, 8)
        self.textures[TextureId.COIN_SMALL_3] = rl.Rectangle(124, 262, 5, 8)

        self.textures[TextureId.ONE_UP] = rl.Rectangle(136, 204, TILE_SIZE, TILE_SIZE)

        self.textures[TextureId.ONE_UP_LABEL] = rl.Rectangle(184, 271, 16, 7)
        self.textures[TextureId.ONEHUNDRED] = rl.Rectangle(153, 287, 11, 8)
        self.textures[TextureId.TWOHUNDRED] = rl.Rectangle(153, 279, 12, 8)
        self.textures[TextureId.THOUSAND] = rl.Rectangle(153, 287, 15, 8)
        self.textures[TextureId.MARIO_FLAG_1] = rl.Rectangle(170, 170, TILE_SIZE, TILE_SIZE)
        self.textures[TextureId.MARIO_FLAG_2] = rl.Rectangle(187, 170, TILE_SIZE, TILE_SIZE)


    def render_texture(self, texture_id: TextureId, dst_rect: rl.Rectangle, flip_h: bool, flip_v: bool) -> None:
        texture = self.textures.get(texture_id)
        if texture:
            # Defina a largura e altura se forem zero
            if dst_rect.width == 0:
                dst_rect.width = texture.width
            if dst_rect.height == 0:
                dst_rect.height = texture.height

            # Renderizar a textura
            rl.draw_texture_ex(texture, (dst_rect.x, dst_rect.y), 0, 1, rl.WHITE)

    def __del__(self):
        """Libera a textura ao final do uso."""
        rl.unload_texture(self.texture)
