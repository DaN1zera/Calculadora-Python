import calculadora_modulos

while True:
    calculadora = calculadora_modulos.Calculadora()
    chamada = int(
        input(
            'Soma(0)'
            '\nSubtração(1)'
            '\nMultiplicação(2)'
            '\nDivisão(3)'
            '\nBhaskara(4)'
            '\nEscolha a operação que deseja fazer: '
        )
    )
    while chamada > 4:
        print('\nVoce escolheu uma opção que não existe')
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

    continua = input('Deseja fazer uma nova operação? s/n: ')
    while continua != 's' and continua != 'n':
        continua = input('Responda com s ou n? s/n: ')
    if continua == 'n':
        break
