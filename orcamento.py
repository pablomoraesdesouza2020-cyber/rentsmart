from utils import moeda


class Orcamento:
    TAXA_CONTRATUAL = 2000.0
    MAX_PARCELAS = 5
    MESES_PROJECAO = 12

    def __init__(self, imovel, parcelas):
        if not 1 <= parcelas <= self.MAX_PARCELAS:
            raise ValueError(f"A taxa pode ser paga em 1 a {self.MAX_PARCELAS} parcelas.")
        self._imovel = imovel
        self._parcelas = parcelas

    @property
    def imovel(self):
        return self._imovel

    @property
    def parcelas(self):
        return self._parcelas

    def aluguel_mensal(self):
        return self._imovel.calcular_aluguel()

    def parcelas_taxa(self):
        valor = round(self.TAXA_CONTRATUAL / self._parcelas, 2)
        lista = [valor] * (self._parcelas - 1)
        lista.append(round(self.TAXA_CONTRATUAL - sum(lista), 2))
        return lista

    def projecao_12_meses(self):
        aluguel = self.aluguel_mensal()
        parcelas = self.parcelas_taxa()
        projecao = []
        for mes in range(1, self.MESES_PROJECAO + 1):
            parcela = parcelas[mes - 1] if mes <= self._parcelas else 0.0
            projecao.append({
                "mes": mes,
                "aluguel": aluguel,
                "parcela_taxa": parcela,
                "total_mes": round(aluguel + parcela, 2),
            })
        return projecao

    def total_12_meses(self):
        return round(sum(linha["total_mes"] for linha in self.projecao_12_meses()), 2)

    def resumo(self):
        largura = 52
        linhas = []
        linhas.append("=" * largura)
        linhas.append("  ORÇAMENTO RENTSMART - R.M IMÓVEIS")
        linhas.append("=" * largura)
        linhas.append(f"Imóvel: {self._imovel.descricao()}")
        linhas.append("")
        linhas.append("--- Composição do aluguel mensal ---")
        for descricao, valor in self._imovel.itens():
            linhas.append(f"{descricao:<36}{moeda(valor):>16}")
        desconto = self._imovel.desconto()
        if desconto is not None:
            linhas.append(f"{'Subtotal':<36}{moeda(self._imovel.subtotal()):>16}")
            linhas.append(f"{desconto[0]:<36}{'- ' + moeda(desconto[1]):>16}")
        linhas.append("-" * largura)
        linhas.append(f"{'ALUGUEL MENSAL':<36}{moeda(self.aluguel_mensal()):>16}")
        linhas.append("")
        linhas.append("--- Taxa contratual (cobrada à parte) ---")
        parcelas = self.parcelas_taxa()
        linhas.append(f"{'Valor total da taxa':<36}{moeda(self.TAXA_CONTRATUAL):>16}")
        linhas.append(f"{'Parcelamento':<36}{str(self._parcelas) + 'x de ' + moeda(parcelas[0]):>16}")
        linhas.append("")
        linhas.append("--- Projeção do primeiro ano ---")
        periodo = "Mês 1" if self._parcelas == 1 else f"Meses 1 a {self._parcelas}"
        linhas.append(
            f"{periodo + ' (aluguel + parcela)':<36}"
            f"{moeda(round(self.aluguel_mensal() + parcelas[0], 2)):>16}"
        )
        if self._parcelas < self.MESES_PROJECAO:
            inicio = self._parcelas + 1
            periodo2 = "Mês 12" if inicio == 12 else f"Meses {inicio} a 12"
            linhas.append(
                f"{periodo2 + ' (só aluguel)':<36}"
                f"{moeda(self.aluguel_mensal()):>16}"
            )
        linhas.append("-" * largura)
        linhas.append(f"{'TOTAL EM 12 MESES':<36}{moeda(self.total_12_meses()):>16}")
        linhas.append("=" * largura)
        return "\n".join(linhas)
