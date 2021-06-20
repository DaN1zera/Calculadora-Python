class Calculadora:
    def bhaskara(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        c = float(input('insira o valor de c: '))
        delta = (b * b) - 4 * (a * c)
        x1 = (-(b) + float(delta) ** 0.5) / (2 * a)
        x2 = (-(b) - float(delta) ** 0.5) / (2 * a)
        print('Valor de delta: {}'.format(delta))
        print('Valor de x1: {}'.format(x1))
        print('Valor de x2: {}'.format(x2))
        return input('\nAperte "enter" para fechar o programa ')

    def soma(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        soma = a + b
        print('Resultado: {}'.format(soma))
        return input('\nAperte "enter" para fechar o programa ')

    def subtracao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        subtracao = a - b
        print('Resultado: {}'.format(subtracao))
        return input('\nAperte "enter" para fechar o programa ')

    def multiplicacao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        multiplicacao = a * b
        print('Resultado: {}'.format(multiplicacao))
        return input('\nAperte "enter" para fechar o programa ')

    def divisao(self):
        a = float(input('insira o valor de a: '))
        b = float(input('insira o valor de b: '))
        divisao = a / b
        print('Resultado: {}'.format(divisao))
        return input('\nAperte "enter" para fechar o programa ')
