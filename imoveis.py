class Imovel:
    TIPO = "Imóvel"
    ALUGUEL_BASE = 0.0

    def itens(self):
        return [(f"Aluguel-base ({self.TIPO})", self.ALUGUEL_BASE)]

    def subtotal(self):
        return round(sum(valor for _, valor in self.itens()), 2)

    def desconto(self):
        return None

    def calcular_aluguel(self):
        total = self.subtotal()
        desconto = self.desconto()
        if desconto is not None:
            total -= desconto[1]
        return round(total, 2)

    def descricao(self):
        return self.TIPO


class ImovelResidencial(Imovel):
    ADICIONAL_2_QUARTOS = 0.0
    VALOR_GARAGEM = 300.0

    def __init__(self, quartos, garagem):
        if quartos not in (1, 2):
            raise ValueError("O imóvel deve ter 1 ou 2 quartos.")
        self._quartos = quartos
        self._garagem = bool(garagem)

    @property
    def quartos(self):
        return self._quartos

    @property
    def garagem(self):
        return self._garagem

    def itens(self):
        itens = super().itens()
        if self._quartos == 2:
            itens.append(("Adicional de 2 quartos", self.ADICIONAL_2_QUARTOS))
        if self._garagem:
            itens.append(("Vaga de garagem", self.VALOR_GARAGEM))
        return itens

    def descricao(self):
        garagem = "com garagem" if self._garagem else "sem garagem"
        return f"{self.TIPO} de {self._quartos} quarto(s), {garagem}"


class Apartamento(ImovelResidencial):
    TIPO = "Apartamento"
    ALUGUEL_BASE = 700.0
    ADICIONAL_2_QUARTOS = 200.0
    PERCENTUAL_DESCONTO = 0.05

    def __init__(self, quartos, garagem, tem_criancas):
        super().__init__(quartos, garagem)
        self._tem_criancas = bool(tem_criancas)

    @property
    def tem_criancas(self):
        return self._tem_criancas

    def desconto(self):
        if not self._tem_criancas:
            valor = round(self.subtotal() * self.PERCENTUAL_DESCONTO, 2)
            return ("Desconto de 5% (sem crianças)", valor)
        return None

    def descricao(self):
        criancas = "com crianças" if self._tem_criancas else "sem crianças"
        return f"{super().descricao()}, {criancas}"


class Casa(ImovelResidencial):
    TIPO = "Casa"
    ALUGUEL_BASE = 900.0
    ADICIONAL_2_QUARTOS = 250.0


class Estudio(Imovel):
    TIPO = "Estúdio"
    ALUGUEL_BASE = 1200.0
    VAGAS_PACOTE = 2
    VALOR_PACOTE = 250.0
    VALOR_VAGA_EXTRA = 60.0

    def __init__(self, vagas):
        if vagas != 0 and vagas < self.VAGAS_PACOTE:
            raise ValueError(
                f"O estacionamento começa no pacote de {self.VAGAS_PACOTE} vagas."
            )
        self._vagas = vagas

    @property
    def vagas(self):
        return self._vagas

    def itens(self):
        itens = super().itens()
        if self._vagas > 0:
            itens.append((f"Pacote de {self.VAGAS_PACOTE} vagas", self.VALOR_PACOTE))
            extras = self._vagas - self.VAGAS_PACOTE
            if extras > 0:
                itens.append(
                    (f"{extras} vaga(s) adicional(is) x R$ 60,00",
                     extras * self.VALOR_VAGA_EXTRA)
                )
        return itens

    def descricao(self):
        if self._vagas == 0:
            return f"{self.TIPO}, sem estacionamento"
        return f"{self.TIPO} com {self._vagas} vaga(s) de estacionamento"
