from abc import ABC, abstractmethod


class PrecoComponent(ABC):
    @abstractmethod
    def preco(self) -> float:
        pass


class PrecoBase(PrecoComponent):
    def __init__(self, preco_base: float):
        self._preco = preco_base

    def preco(self) -> float:
        return self._preco


class PrecoDecorator(PrecoComponent):
    def __init__(self, componente: PrecoComponent):
        self._componente = componente

    def preco(self) -> float:
        return self._componente.preco()