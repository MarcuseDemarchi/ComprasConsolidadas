from .base import CalculoPreco
from domain.models import Proposta
from typing import List


class ScoreMultifator(CalculoPreco):
    def avaliar(self, propostas: List[Proposta]):
    # Exemplo: score composto por preco e score fornecido (maior é melhor)
    # Transformamos preco em um valor onde menor preco => maior pontuacao
        max_preco = max((p.preco_unitario * p.quantidade) for p in propostas)
        scored = []
        for p in propostas:
            preco_total = p.preco_unitario * p.quantidade
            preco_score = (max_preco - preco_total) / max_preco if max_preco else 0
            total_score = 0.6 * preco_score + 0.4 * (p.score or 0)
            scored.append((total_score, p))
        return [p for _, p in sorted(scored, key=lambda t: t[0], reverse=True)]