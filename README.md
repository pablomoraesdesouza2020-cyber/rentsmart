# RentSmart — Sistema de Orçamento de Locação

O RentSmart é uma aplicação em Python desenvolvida para a disciplina Algorithmic Thinking & Introduction to Object-Oriented Programming. O sistema calcula orçamentos de locação para apartamentos, casas e estúdios pelo terminal, aplicando automaticamente adicionais, descontos e taxa contratual, e gera um arquivo CSV com a projeção dos 12 primeiros meses.

## Como executar

É necessário ter o Python 3.8 ou superior instalado. Não há bibliotecas externas.


git clone https://github.com/pablomoraesdesouza2020-cyber/rentsmart.git
cd rentsmart
python main.py


No Windows, se python não funcionar, use py main.py.

O programa faz as perguntas no terminal, mostra o orçamento detalhado e salva o arquivo projecao_12_meses.csv na mesma pasta. Se forem feitos vários orçamentos na mesma execução, os arquivos seguintes são numerados (projecao_12_meses_2.csv, e assim por diante).

## Regras de negócio

Valores-base mensais: apartamento R$ 700, casa R$ 900 e estúdio R$ 1.200.

O segundo quarto acrescenta R$ 200 no apartamento e R$ 250 na casa. A garagem de casa e apartamento acrescenta R$ 300.

No estúdio, o estacionamento é opcional e começa em um pacote de 2 vagas por R$ 250, com R$ 60 por vaga extra.

Apartamentos sem crianças recebem 5% de desconto sobre o aluguel já com os adicionais.

A taxa contratual é de R$ 2.000, cobrada à parte, em até 5 parcelas iguais nos primeiros meses. Diferenças de centavos são ajustadas na última parcela.

## Estrutura do código

main.py conduz o fluxo do programa. entrada.py lê e valida os dados digitados. imoveis.py contém as classes dos imóveis e o cálculo do aluguel. orcamento.py contém a classe Orcamento, que une aluguel e taxa e monta a projeção de 12 meses. exportador.py gera o CSV. utils.py formata os valores em reais.

## Orientação a Objetos

Apartamento e Casa herdam de ImovelResidencial, que herda de Imovel. Estudio herda diretamente de Imovel.

Os atributos são protegidos (como _quartos e _vagas), com validação no construtor e acesso por @property.

Cada classe define a própria forma de calcular o aluguel. Por isso, o Orcamento funciona do mesmo jeito para qualquer tipo de imóvel.

## Arquivo CSV

O arquivo usa ponto e vírgula como separador e vírgula como decimal, para abrir direto no Excel em português. Cada linha é um mês, com as colunas mes, aluguel, parcela_taxa e total_mes, e uma linha final com o total.

## Autor

Pablo — Ciencias da Computação