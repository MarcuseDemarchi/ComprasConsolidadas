from typing import Optional
from strategies.base import CalculoPreco
from strategies.menor_preco import MenorPreco
from strategies.score_multifator import ScoreMultifator
from strategies.por_lote import PorLote


class StrategyFactory:
    @staticmethod
    def create(name: str) -> Optional[CalculoPreco]:
        name = (name or '').lower()
        if name == 'menor_preco':
            return MenorPreco()
        if name == 'score_multifator':
            return ScoreMultifator()
        if name == 'por_lote':
            return PorLote()
        return None