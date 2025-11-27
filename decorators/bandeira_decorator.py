from .base import PrecoDecorator, PrecoComponent


class BandeiraDecorator(PrecoDecorator):
    def __init__(self, componente: PrecoComponent, taxa_percentual: float):
        super().__init__(componente)
        self.taxa = taxa_percentual

    def preco(self) -> float:
        base = self._componente.preco()
        return base * (1 + self.taxa / 100)