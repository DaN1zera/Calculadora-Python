import calculadora_modulos

calculadora = calculadora_modulos.Calculadora()
chamada = int(
    input(
        'Soma(0)'
        '\nSubtracao(1)'
        '\nMultiplicacao(2)'
        '\nDivisao(3)'
        '\nBhaskara(4)'
        '\nEscolha a operacao que deseja fazer: '
    )
)
while chamada > 4:
    print('\nVoce escolheu uma opcao que nao existe')
    chamada = int(input('Tente novamente: '))

if chamada == 0:
    print(calculadora.soma())
elif chamada == 1:
    print(calculadora.subtracao())
elif chamada == 2:
    print(calculadora.multiplicacao())
elif chamada == 3:
    print(calculadora.divisao())
elif chamada == 4:
    print(calculadora.bhaskara())
