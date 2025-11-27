from .observer_base import Observer
from observers.notifier import Event
from infra.singletons import Logger


class LogObserver(Observer):
    def update(self, event: Event):
        logger = Logger.get_instance()
        logger.log(f"[EVENT] tipo={event.tipo} payload={event.payload}")