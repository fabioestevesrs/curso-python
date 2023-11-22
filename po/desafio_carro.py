class Carro:
    def __init__(self, velocidadeMaxima):
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidadeAtual = 0

    def acelerar(self, delta=5):
        self.velocidadeAtual += delta

        if self.velocidadeAtual > self.velocidadeMaxima:
            self.velocidadeAtual = self.velocidadeMaxima
            print('Atingiu a velocidade máxima!')

        return self.velocidadeAtual

    def frear(self, delta=5):
        self.velocidadeAtual -= delta

        if self.velocidadeAtual < 0:
            self.velocidadeAtual = 0

        return self.velocidadeAtual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print('Acelerando...')
        print(f'Velocidade atual: {c1.acelerar(8)}')

    for _ in range(20):
        velocidadeAtual = c1.frear(delta=20)

        if velocidadeAtual > 0:
            print('Freando...')
            print(f'Velocidade atual: {velocidadeAtual}')
        else:
            print('Carro parado!')
            break
