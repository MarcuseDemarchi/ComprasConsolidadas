from typing import Any, Dict, List


class Event:
    def __init__(self, tipo: str, payload: Dict[str, Any]):
        self.tipo = tipo
        self.payload = payload

class Notifier:
    def __init__(self):
        self._observers = []

    def register(self, obs):
        self._observers.append(obs)

    def unregister(self, obs):
        self._observers.remove(obs)

    def notify(self, event: Event):
        for o in list(self._observers):
            o.update(event)