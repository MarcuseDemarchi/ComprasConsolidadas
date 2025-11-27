# Compras Consolidadas --- Sistema com Design Patterns

**Autor:** Marcus André Geacomo Demarchi\
**Repositório GitHub:**
https://github.com/MarcuseDemarchi/ComprasConsolidadas.git

------------------------------------------------------------------------

## 📌 Sobre o Projeto

Este sistema implementa um fluxo simplificado de **Compras
Consolidadas**, onde diversas propostas de compra são reunidas em uma
única rodada e avaliadas por meio de regras de cálculo configuráveis.\
O programa permite cadastrar propostas, aplicar estratégias de decisão,
decorar valores com descontos/taxas e notificar observadores sobre
eventos importantes.

O projeto utiliza **3 padrões de projeto obrigatórios**:

-   **Strategy**\
-   **Observer**\
-   **Decorator**\
-   **Factory Method**\
-   **Singleton**

E está organizado nas pastas:

    domain/
    strategies/
    decorators/
    observers/
    factory/
    infra/
    app/
    tests/
    docs/

------------------------------------------------------------------------

# 🎯 Objetivo do Sistema

Permitir que um grupo de pessoas envie propostas de compra e que o
sistema determine automaticamente qual é a melhor opção utilizando
estratégias selecionáveis pelo usuário.

Casos reais de uso: - Compra conjunta de suprimentos em empresas\
- Grupos de WhatsApp comprando alimentos no atacado\
- Condomínios centralizando compras de limpeza\
- ONGs comprando ração ao menor custo

------------------------------------------------------------------------

# 🧩 Padrões de Projeto Utilizados

------------------------------------------------------------------------

# 1️⃣ Strategy --- Seleção da Melhor Proposta

### ✔ **Motivação**

As regras de escolha da melhor proposta podem variar: menor preço,
melhor média, maior quantidade etc.\
O padrão **Strategy** permite trocar a regra em tempo de execução sem
alterar o código da aplicação.

### ✔ **Como foi aplicado**

Interface: `BaseStrategy`\
Implementações: - `MenorPrecoStrategy` - `MediaPrecoStrategy` -
`MaiorQuantidadeStrategy`

Contexto usando Strategy:\
`StrategyFactory.create_strategy(tipo)`

### ✔ **Ponto forte demonstrado**

A **troca dinâmica de estratégias** durante a execução.

------------------------------------------------------------------------

# 2️⃣ Decorator --- Modificações no Preço Final

### ✔ **Motivação**

O valor final pode ser alterado por: - cupons de desconto\
- taxas extras\
- bandeiras\
- cashback

O padrão **Decorator** permite adicionar essas funcionalidades sem
modificar o preço base.

### ✔ **Como foi aplicado**

Component base: `PrecoBase`\
Decorators: - `CupomDecorator` - `TaxaDecorator`

### ✔ **Ponto forte demonstrado**

A composição de múltiplos decoradores para modificar o preço:

``` python
preco = CupomDecorator(TaxaDecorator(PrecoBase(valor)))
```

------------------------------------------------------------------------

# 3️⃣ Observer --- Notificações de Eventos

### ✔ **Motivação**

Quando uma rodada é consolidada, o sistema precisa avisar: - loggers\
- listeners\
- services externos

Sem acoplamento direto.

### ✔ **Como foi aplicado**

-   `Notifier` (Subject)
-   `LogObserver` (Observer)
-   Eventos enviados: `Event(tipo, payload)`

### ✔ **Ponto forte demonstrado**

Vários observers são notificados automaticamente quando a rodada é
encerrada.

------------------------------------------------------------------------

# 4️⃣ Factory Method --- Criação de Estratégias

### ✔ **Motivação**

Usuário escolhe o tipo de cálculo por string.\
Precisamos criar dinamicamente a Strategy correspondente.

### ✔ **Como foi aplicado**

`StrategyFactory.create_strategy(tipo)`\
Retorna a implementação correta da estratégia.

------------------------------------------------------------------------

# 5️⃣ Singleton --- Config e Logger

### ✔ **Motivação**

Evitar múltiplas instâncias de configurações e logger.

### ✔ **Como foi aplicado**

Classes: - `Config` - `Logger`

Ambas garantem que existe **apenas 1 instância**.

Testes comprovam unicidade.

------------------------------------------------------------------------

# 📐 Diagrama UML Simplificado (Mermaid)

``` mermaid
classDiagram

class Rodada {
  +propostas
  +add_proposta()
  +consolidar(strategy)
}

class Proposta {
  +nome
  +valor
  +quantidade
}

class BaseStrategy {
  <<interface>>
  +calcular(propostas)
}

BaseStrategy <|-- MenorPrecoStrategy
BaseStrategy <|-- MediaPrecoStrategy
BaseStrategy <|-- MaiorQuantidadeStrategy

class PrecoBase {
  +calcular()
}

class Decorator {
  <<abstract>>
  +component
  +calcular()
}

Decorator <|-- CupomDecorator
Decorator <|-- TaxaDecorator

class Notifier {
  +observers
  +register()
  +notify(event)
}

class LogObserver {
  +update(event)
}

class StrategyFactory {
  +create_strategy(tipo)
}
```

------------------------------------------------------------------------

# ▶ Como Executar

### 1. Clonar o repositório

``` bash
git clone https://github.com/MarcuseDemarchi/ComprasConsolidadas.git
cd ComprasConsolidadas
```

### 2. Rodar o programa principal

``` bash
python app/main.py
```

------------------------------------------------------------------------

# ▶ Como Usar (Fluxo no Terminal)

### 1. Criar rodada

### 2. Adicionar propostas

### 3. Escolher strategy

### 4. Aplicar decoradores (opcional)

### 5. Consolidar

### 6. Observers são notificados automaticamente

------------------------------------------------------------------------

# 🧪 Testes Automatizados

Para rodar os testes:

``` bash
pytest
```

Testes cobrem:

-   troca de estratégias\
-   composição de decoradores\
-   notificação de observers\
-   criação via Factory\
-   unicidade do Singleton

------------------------------------------------------------------------

# 📌 Decisões de Design

✔ Baixo acoplamento entre camadas\
✔ Padrões aplicados em locais naturais do domínio\
✔ CLI simples para demonstração acadêmica\
✔ Readability priorizada\
✔ Domínio adaptado para regras dinâmicas de avaliação de propostas

------------------------------------------------------------------------

# 📌 Limitações

❗ Sistema não persiste dados\
❗ Não possui interface web\
❗ Simples por natureza acadêmica

------------------------------------------------------------------------

# 📌 Próximos Passos

-   Adicionar API REST com FastAPI\
-   Adicionar banco SQLite\
-   Adicionar autenticação\
-   Criar dashboard web

------------------------------------------------------------------------

# ✔ Rodapé obrigatório

Sempre que a CLI é exibida, o rodapé mostra:

    Desenvolvido por: Marcus André Geacomo Demarchi

------------------------------------------------------------------------
