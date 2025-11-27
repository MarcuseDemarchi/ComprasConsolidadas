from .base import PrecoDecorator, PrecoComponent


class CupomDecorator(PrecoDecorator):
    def __init__(self, componente: PrecoComponent, desconto_percentual: float):
        super().__init__(componente)
        self.desconto = desconto_percentual

    def preco(self) -> float:
        base = self._componente.preco()
        return base * (1 - self.desconto / 100)