"""
app/main.py

CLI simples que demonstra os padrões e exibe o rodapé com autor.
Salve em app/main.py e execute: python -m app.main
"""
from typing import List
import sys

from domain.models import Proposta, Rodada
from factory.strategy_factory import StrategyFactory
from infra.singletons import Config, Logger
from observers.notifier import Notifier, Event
from observers.log_observer import LogObserver
from decorators.base import PrecoBase
from decorators.cupom_decorator import CupomDecorator
from decorators.bandeira_decorator import BandeiraDecorator


def criar_propostas_exemplo() -> List[Proposta]:
    return [
        Proposta('Fornecedor A', preco_unitario=10.0, quantidade=5, score=0.8),
        Proposta('Fornecedor B', preco_unitario=9.5, quantidade=5, score=0.7),
        Proposta('Fornecedor C', preco_unitario=11.0, quantidade=10, score=0.9),
    ]


class App:
    def __init__(self):
        self.logger = Logger.get_instance()
        self.cfg = Config.get_instance()
        self.notifier = Notifier()
        # Registrar observers padrão
        self.notifier.register(LogObserver())

        # estado simples do app
        self.rodada: Rodada = Rodada('r1', criar_propostas_exemplo(), aberta=True)

    def mostrar_menu(self):
        print("\n=== Compras Consolidadas (CLI) ===")
        print("1) Mostrar propostas")
        print("2) Avaliar propostas (usar Strategy atual: {})".format(self.cfg.strategy))
        print("3) Trocar Strategy (Factory)")
        print("4) Aplicar decoradores ao vencedor (cupom + bandeira)")
        print("5) Fechar rodada (notifica observers)")
        print("6) Adicionar observer de teste (LogObserver)")
        print("0) Sair")
        print("\n---")
        print("Desenvolvido por: Marcus André Geacomo Demarchi")
        print("===============================\n")

    def mostrar_propostas(self):
        print(f"Rodada {self.rodada.id} - aberta={self.rodada.aberta}")
        for p in self.rodada.propostas:
            print(f"- {p.fornecedor} | unit: {p.preco_unitario:.2f} | qty: {p.quantidade} | score:{p.score}")

    def avaliar_propostas(self):
        strategy = StrategyFactory.create(self.cfg.strategy)
        if not strategy:
            self.logger.log(f"[ERRO] Strategy '{self.cfg.strategy}' não encontrada pela Factory.")
            return
        ordenadas = strategy.avaliar(self.rodada.propostas)
        self.logger.log("Propostas ordenadas (melhor primeiro):")
        for idx, p in enumerate(ordenadas, start=1):
            total = p.preco_unitario * p.quantidade
            self.logger.log(f"{idx}) {p.fornecedor} - total={total:.2f} (unit={p.preco_unitario:.2f} qty={p.quantidade})")
        return ordenadas

    def trocar_strategy(self):
        print("Opções disponíveis: menor_preco, score_multifator, por_lote")
        nova = input("Digite o nome da strategy desejada: ").strip()
        if StrategyFactory.create(nova) is None:
            print(f"Strategy '{nova}' não reconhecida.")
            return
        self.cfg.strategy = nova
        self.logger.log(f"Strategy alterada para '{nova}' (Config singleton).")

    def aplicar_decoradores_vencedor(self):
        ordenadas = self.avaliar_propostas()
        if not ordenadas:
            print("Nenhuma proposta avaliada.")
            return
        escolhido = ordenadas[0]
        preco_base_valor = escolhido.preco_unitario * escolhido.quantidade
        preco_base = PrecoBase(preco_base_valor)
        # pedir valores simples ao usuário
        try:
            desconto = float(input("Informe desconto de cupom (%) (ex: 5): ").strip() or "0")
        except ValueError:
            desconto = 0.0
        try:
            taxa = float(input("Informe taxa de bandeira (%) (ex: 2): ").strip() or "0")
        except ValueError:
            taxa = 0.0

        com_cupom = CupomDecorator(preco_base, desconto_percentual=desconto)
        com_bandeira = BandeiraDecorator(com_cupom, taxa_percentual=taxa)
        preco_final = com_bandeira.preco()

        self.logger.log(f"Vencedor: {escolhido.fornecedor}")
        self.logger.log(f"Preço base: {preco_base_valor:.2f}")
        self.logger.log(f"Preço final após Cupom({desconto}%) + Bandeira({taxa}%): {preco_final:.2f}")

    def fechar_rodada(self):
        if not self.rodada.aberta:
            print("Rodada já está fechada.")
            return
        self.rodada.aberta = False
        self.notifier.notify(Event('rodada_fechada', {'rodada_id': self.rodada.id}))
        self.logger.log(f"Rodada {self.rodada.id} foi fechada e observers notificados.")

    def adicionar_observer_teste(self):
        # exemplo de adicionar outro LogObserver (poderia ter EmailObserver, WebhookObserver, etc)
        self.notifier.register(LogObserver())
        self.logger.log("LogObserver adicional registrado (para teste).")

    def loop(self):
        while True:
            self.mostrar_menu()
            opc = input("Escolha uma opção: ").strip()
            if opc == "1":
                self.mostrar_propostas()
            elif opc == "2":
                self.avaliar_propostas()
            elif opc == "3":
                self.trocar_strategy()
            elif opc == "4":
                self.aplicar_decoradores_vencedor()
            elif opc == "5":
                self.fechar_rodada()
            elif opc == "6":
                self.adicionar_observer_teste()
            elif opc == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


def main():
    app = App()
    try:
        app.loop()
    except KeyboardInterrupt:
        print("\nInterrupção pelo usuário. Saindo...")
        sys.exit(0)


if __name__ == "__main__":
    main()
