import pyray as rl # type: ignore
from pyray import Vector2
import math

import sys
print(sys.version)

# Constants for physics
WALK_ACC = (9.0 / 256 + 8.0 / (16 * 16 * 16)) * 60 * 60
RUN_ACC = (14.0 / 256 + 4.0 / (16 * 16 * 16)) * 60 * 60
MIN_WALK = (1.0 / 16 + 3.0 / 256) * 60
MAX_WALK = (1 + 9.0 / 16) * 60
MAX_RUN = (2 + 9.0 / 16) * 60
RELEASE_DEACC = (13.0 / 256) * 60 * 60
SKID_DEACC = (1.0 / 16 + 10.0 / 256) * 60 * 60
TURN_THRESHOLD = (9.0 / 16) * 60

# Gravity and Jump
JUMP_SPD = 4.0 * 60
BIG_JUMP_SPD = 5.0 * 60
SMALL_GRAVITY = (7.0 / 16) * 60 * 60
BIG_GRAVITY = (9.0 / 16) * 60 * 60
MAX_FALL = 4.0 * 60

# Global variables
velocity = Vector2(0, 0)
position = Vector2(100, 300)  # Initial position
direction = 0.0
is_grounded = True
input_jump = False
input_jump_p = False
acc = 0.0
is_skidding = False

def handle_input():
    global direction, input_jump

    # Input for movement
    if rl.is_key_down(rl.KEY_RIGHT):
        direction = 1.0
    elif rl.is_key_down(rl.KEY_LEFT):
        direction = -1.0
    else:
        direction = 0.0

    # Jump input
    input_jump = rl.is_key_down(rl.KEY_SPACE)

def update_physics(delta):
    global velocity, is_grounded, acc, is_skidding, input_jump_p

    # Direção horizontal
    if is_grounded:
        velocity.y = SMALL_GRAVITY * delta

        if abs(direction) > 0.01:
            if direction * velocity.x < 0:  # Virando enquanto se move
                is_skidding = abs(velocity.x) > TURN_THRESHOLD
                velocity.x += SKID_DEACC * direction * delta
            else:
                acc = RUN_ACC if rl.is_key_down(rl.KEY_LEFT_SHIFT) else WALK_ACC
                velocity.x += acc * direction * delta
                velocity.x = clamp(velocity.x, -MAX_RUN, MAX_RUN)

        # Desaceleração ao soltar as teclas
        else:
            if abs(velocity.x) < RELEASE_DEACC * delta:
                velocity.x = 0
            else:
                velocity.x -= RELEASE_DEACC * math.copysign(1, velocity.x) * delta

        # Pulo
        if input_jump and not input_jump_p:
            velocity.y = -BIG_JUMP_SPD

    # No ar (controle midair)
    else:
        if abs(direction) > 0.01:
            if abs(velocity.x) >= MAX_WALK:
                velocity.x += RUN_ACC * direction * delta
            else:
                velocity.x += WALK_ACC * direction * delta

        # Gravetidade no ar
        velocity.y += SMALL_GRAVITY * delta

        if velocity.y > MAX_FALL:
            velocity.y = MAX_FALL

    # Salvar estado do botão de pulo
    input_jump_p = input_jump

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def draw_character():
    rl.draw_rectangle(int(position.x), int(position.y), 20, 40, rl.BLUE)

def move_and_slide():
    global position, velocity
    # Atualiza a posição com base na velocidade
    position.x += velocity.x * rl.get_frame_time()
    position.y += velocity.y * rl.get_frame_time()

rl.init_window(800, 600, "Mario Physics Clone")
rl.set_target_fps(60)

while not rl.window_should_close():
    # Atualizar entrada e física
    handle_input()
    update_physics(rl.get_frame_time())

    # Atualizar posição
    move_and_slide()

    # Desenhar
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    draw_character()
    rl.end_drawing()

rl.close_window()
