from math import pi


def circulo(raio):
    calculo = pi * (float(raio) ** 2)
    print(f'Cálculo = {calculo}')


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
