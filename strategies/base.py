from abc import ABC, abstractmethod
from typing import List
from domain.models import Proposta


class CalculoPreco(ABC):
    @abstractmethod
    def avaliar(self, propostas: List[Proposta]):
        """Retorna lista de propostas com algum criterio de ordenação/score."""
        pass