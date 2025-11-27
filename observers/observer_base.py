from abc import ABC, abstractmethod
from observers.notifier import Event


class Observer(ABC):
    @abstractmethod
    def update(self, event: Event):
        pass