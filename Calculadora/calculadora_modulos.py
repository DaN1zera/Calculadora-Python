import colorama
from colorama import Fore

branco = Fore.WHITE
vermelho = Fore.RED
azul = Fore.BLUE
verde = Fore.GREEN


class Calculadora:
    def bhaskara(self):
        print(azul + '========Bhaskara========')
        a = float(input(f'{branco}insira o valor de a: {vermelho}'))
        b = float(input(f'{branco}insira o valor de b: {vermelho}'))
        c = float(input(f'{branco}insira o valor de c: {vermelho}'))
        delta = (b * b) - 4 * (a * c)
        x1 = (-(b) + float(delta) ** 0.5) / (2 * a)
        x2 = (-(b) - float(delta) ** 0.5) / (2 * a)
        print(f'{branco}Valor de delta:{verde} {delta}')
        print(f'{branco}Valor de x1:{verde} {x1}')
        print(f'{branco}Valor de x2:{verde} {x2}')
        return input(branco + 'Aperte "enter" para continuar ')

    def soma(self):
        print(azul + '========Soma========')
        a = float(input(f'{branco}insira o valor de a: {vermelho}'))
        b = float(input(f'{branco}insira o valor de b: {vermelho}'))
        soma = a + b
        print(f'{branco}Resultado:{verde} {soma}')
        return input(branco + 'Aperte "enter" para continuar ')

    def subtracao(self):
        print(azul + '========Subtração========')
        a = float(input(f'{branco}insira o valor de a: {vermelho}'))
        b = float(input(f'{branco}insira o valor de b: {vermelho}'))
        subtracao = a - b
        print(f'{branco}Resultado:{verde} {subtracao}')
        return input(branco + 'Aperte "enter" para continuar ')

    def multiplicacao(self):
        print(azul + '========Multiplicação========')
        a = float(input(f'{branco}insira o valor de a: {vermelho}'))
        b = float(input(f'{branco}insira o valor de b: {vermelho}'))
        multiplicacao = a * b
        print(f'{branco}Resultado:{verde} {multiplicacao}')
        return input(branco + 'Aperte "enter" para continuar ')

    def divisao(self):
        print(azul + '========Divisão========')
        a = float(input(f'{branco}insira o valor de a: {vermelho}'))
        b = float(input(f'{branco}insira o valor de b: {vermelho}'))
        divisao = a / b
        resto = a % b
        print(f'{branco}Resultado:{verde} {divisao}')
        print(f'{branco}Resto:{verde} {resto}')
        return input(branco + 'Aperte "enter" para continuar ')

    def cateto(self):
        return 0
