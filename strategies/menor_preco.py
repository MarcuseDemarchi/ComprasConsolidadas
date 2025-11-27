from .base import CalculoPreco
from domain.models import Proposta
from typing import List


class MenorPreco(CalculoPreco):
    def avaliar(self, propostas: List[Proposta]):
        # ordena por preco total crescente
        return sorted(propostas, key=lambda p: p.preco_unitario * p.quantidade)