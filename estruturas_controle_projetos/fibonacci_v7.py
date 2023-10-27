def fibonacci(quantidade_numeros):
    resultado = [0, 1]

    for _ in range(2, quantidade_numeros):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for valor in fibonacci(15):
        print(valor)
