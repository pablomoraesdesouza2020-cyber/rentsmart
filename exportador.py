import csv

CABECALHO = ["mes", "aluguel", "parcela_taxa", "total_mes"]


def _numero(valor):
    return f"{valor:.2f}".replace(".", ",")


def gerar_csv(projecao, caminho):
    with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CABECALHO, delimiter=";")
        escritor.writeheader()
        for linha in projecao:
            escritor.writerow({
                "mes": linha["mes"],
                "aluguel": _numero(linha["aluguel"]),
                "parcela_taxa": _numero(linha["parcela_taxa"]),
                "total_mes": _numero(linha["total_mes"]),
            })
        escritor.writerow({
            "mes": "TOTAL",
            "aluguel": _numero(sum(l["aluguel"] for l in projecao)),
            "parcela_taxa": _numero(sum(l["parcela_taxa"] for l in projecao)),
            "total_mes": _numero(sum(l["total_mes"] for l in projecao)),
        })
    return caminho
