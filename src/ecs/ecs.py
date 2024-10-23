from abc import ABC, abstractmethod
from typing import Dict, List, Type, Callable, Any, Optional

class Component(ABC):
    def __init__(self) -> None:
        pass

class Entity:
    def __init__(self) -> None:
        self.components: Dict[type, Component] = {}

    def assign(self, component_type: Type, *args: Any, **kwargs: Any) -> None:
        component = component_type(*args, **kwargs)
        self.components[component_type] = component

    def remove(self, component_type: Type) -> None:
        self.components.pop(component_type, None)

    def clear_components(self) -> bool:
        self.components.clear()
        return True

    def get(self, component_type: Type) -> Optional[Any]:
        return self.components.get(component_type)

    def has(self, component_type: Type) -> bool:
        return component_type in self.components

    def has_any(self, *component_types: Type) -> bool:
        return any(self.has(component_type) for component_type in component_types)


class System(ABC):
    @abstractmethod
    def tick(self, world) -> None:
        pass  # Método abstrato, deve ser implementado nas subclasses

    def on_added_to_world(self, world) -> None:
        pass  # Método vazio, pode ser sobreposto nas subclasses

    def handle_event(self, event) -> None:
        pass  # Pode ser sobreposto nas subclasses

    def on_removed_from_world(self, world) -> None:
        pass  # Método vazio, pode ser sobreposto nas subclasses


class World:
    def __init__(self) -> None:
        self.systems: List[System] = []
        self.entities: List[Entity] = []

    def create(self) -> Entity:
        e = Entity()
        self.entities.append(e)
        return e

    def destroy(self, entity: Entity) -> None:
        if entity is None:
            return
        self.entities.remove(entity)

    def register_system(self, system_class: Type[System], *args: Any, **kwargs: Any) -> System:
        system = system_class(*args, **kwargs)
        self.systems.append(system)
        system.on_added_to_world(self)
        return system

    def unregister_system(self, system: System) -> None:
        if system is None:
            return
        self.systems.remove(system)
        system.on_removed_from_world(self)

    def find_first(self, *components: Type) -> Optional[Entity]:
        return next((entity for entity in self.entities if entity.has(*components)), None)

    def find(self, *components: Type, callback: Callable[[Entity], None]) -> None:
        for entity in self.entities:
            if entity.has(*components):
                callback(entity)

    def find_any(self, *components: Type, callback: Callable[[Entity], None]) -> None:
        for entity in self.entities:
            if entity.has_any(*components):
                callback(entity)

    def tick(self) -> None:
        for system in self.systems:
            system.tick(self)

    def handle_event(self, event) -> None:
        for system in self.systems:
            system.handle_event(event)
