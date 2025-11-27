from .base import CalculoPreco
from domain.models import Proposta
from typing import List


class PorLote(CalculoPreco):
    def avaliar(self, propostas: List[Proposta]):
        #  Prefere propostas que atendam mais unidades (simples heuristica)
        return sorted(propostas, key=lambda p: (-p.quantidade, p.preco_unitario))