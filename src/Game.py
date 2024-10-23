import pyray as rl # type: ignore
from src.scenes.IntroScene import IntroScene

class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.window = None
        self.event = None
        self.current_scene = None

    def init(self, title, width, height, fullscreen):

        if fullscreen:
            rl.set_config_flags(rl.FLAG_WINDOW_HIGHDPI | rl.FLAG_FULLSCREEN_MODE)
        else:
            rl.set_config_flags(rl.FLAG_WINDOW_HIGHDPI)

        rl.init_window(width, height, title)

        if not rl.window_should_close():
            self.is_running = True
            self.current_scene = IntroScene()  # Criando a cena inicial
        else:
            print("Unable to create window.")
            rl.close_window()

    def handle_events(self):
        pass

    def update(self):
        pass

    def clean(self):
        pass

    def running(self):
        pass

