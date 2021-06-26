import os

import colorama
from colorama import Fore

import calculadora_modulos

calculadora = calculadora_modulos.Calculadora()


os.system('cls')

while True:
    print(Fore.BLUE + '=' * 34, Fore.BLUE + '\n========CALCULADORA PYTHON========')
    print(Fore.BLUE + '=' * 34)
    print()
    chamada = input(Fore.WHITE + 'Soma...........: 0' '\nSubtração......: 1' '\nMultiplicação .: 2' '\nDivisão........: 3' '\nBhaskara.......: 4' '\nEscolha a operação que deseja fazer: ')
    while chamada not in ('0', '1', '2', '3', '4'):
        print('Voce escolheu uma opção que não existe')
        chamada = input('Tente novamente: ')
    os.system('cls')

    if chamada == '0':
        print(calculadora.soma())
    elif chamada == '1':
        print(calculadora.subtracao())
    elif chamada == '2':
        print(calculadora.multiplicacao())
    elif chamada == '3':
        print(calculadora.divisao())
    elif chamada == '4':
        print(calculadora.bhaskara())

    continua = input(Fore.WHITE + 'Deseja fazer uma nova operação?: ').lower()
    while continua not in ('s', 'n', 'sim', 'nao', 'não'):
        continua = input('Responda com Sim ou Não: ')
    if continua == 'n' or continua == 'nao' or continua == 'não':
        os.system('cls')
        break
    os.system('cls')
