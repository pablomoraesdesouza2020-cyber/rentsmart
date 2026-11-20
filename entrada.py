def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Valor fora do intervalo! Digite um número entre {minimo} e {maximo}.")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Resposta inválida! Digite 's' para sim ou 'n' para não.")


def ler_opcao(titulo, opcoes):
    print(f"\n{titulo}")
    for numero, texto in opcoes.items():
        print(f"  {numero} - {texto}")
    return ler_inteiro("Escolha uma opção: ", min(opcoes), max(opcoes))
