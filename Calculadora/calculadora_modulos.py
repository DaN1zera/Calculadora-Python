class Calculadora:
    def bhaskara(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        c = float(input('insira o valor de c: '))
        delta = (b * b) - 4 * (a * c)
        x1 = (-(b) + float(delta) ** 0.5) / (2 * a)
        x2 = (-(b) - float(delta) ** 0.5) / (2 * a)
        print(f'Valor de delta: {delta}')
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')
        return input('Aperte "enter" para continuar ')

    def soma(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        soma = a + b
        print(f'Resultado: {soma}')
        return input('Aperte "enter" para continuar ')

    def subtracao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        subtracao = a - b
        print(f'Resultado: {subtracao}')
        return input('Aperte "enter" para continuar ')

    def multiplicacao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        multiplicacao = a * b
        print(f'Resultado: {multiplicacao}')
        return input('Aperte "enter" para continuar ')

    def divisao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        divisao = a / b
        resto = a % b
        print(f'Resultado: {divisao}')
        print(f'Resto: {resto}')
        return input('Aperte "enter" para continuar ')
