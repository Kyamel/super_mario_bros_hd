from src.ecs.ecs import World

class Scene:
    def __init__(self) -> None:
        self.world = World()

    def update(self):
        self.world.tick()

    def if_finished(self):
        return True

    def handle_events(self, event):
        self.world.handle_event(event)

    def __del__(self):
        print("Scene deleted")
        # Em Python, o garbage collector cuida da liberação de memória
        del self.world