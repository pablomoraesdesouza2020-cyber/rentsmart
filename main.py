from entrada import ler_inteiro, ler_opcao, ler_sim_nao
from exportador import gerar_csv
from imoveis import Apartamento, Casa, Estudio
from orcamento import Orcamento

TIPOS_IMOVEL = {1: "Apartamento", 2: "Casa", 3: "Estúdio"}


def montar_imovel():
    tipo = ler_opcao("Qual tipo de imóvel deseja alugar?", TIPOS_IMOVEL)

    if tipo == 3:
        vagas = 0
        if ler_sim_nao("Deseja estacionamento? (pacote inicial de 2 vagas)"):
            vagas = ler_inteiro("Quantas vagas no total? (mínimo 2, máximo 10): ", 2, 10)
        return Estudio(vagas)

    quartos = ler_inteiro("Quantos quartos? (1 ou 2): ", 1, 2)
    garagem = ler_sim_nao("Deseja vaga de garagem?")

    if tipo == 1:
        tem_criancas = ler_sim_nao("Possui crianças?")
        return Apartamento(quartos, garagem, tem_criancas)
    return Casa(quartos, garagem)


def nome_arquivo_csv(numero):
    if numero == 1:
        return "projecao_12_meses.csv"
    return f"projecao_12_meses_{numero}.csv"


def main():
    print("=" * 52)
    print("  RENTSMART - R.M IMÓVEIS")
    print("  Sistema de orçamento de locação")
    print("=" * 52)

    numero_orcamento = 1
    while True:
        imovel = montar_imovel()
        parcelas = ler_inteiro(
            "\nEm quantas parcelas deseja pagar a taxa contratual de R$ 2.000,00? (1 a 5): ",
            1, 5,
        )
        orcamento = Orcamento(imovel, parcelas)

        print()
        print(orcamento.resumo())

        arquivo = gerar_csv(orcamento.projecao_12_meses(), nome_arquivo_csv(numero_orcamento))
        print(f"\nProjeção de 12 meses salva em: {arquivo}")

        if not ler_sim_nao("\nDeseja fazer outro orçamento?"):
            break
        numero_orcamento += 1

    print("\nObrigado por usar o RentSmart!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPrograma encerrado.")
