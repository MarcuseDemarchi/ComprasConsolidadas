from dataclasses import dataclass
from typing import List


@dataclass
class Proposta:
    fornecedor: str
    preco_unitario: float
    quantidade: int
    score: float = 0.0

@dataclass
class Rodada:
    id: str
    propostas: List[Proposta]
    aberta: bool = True