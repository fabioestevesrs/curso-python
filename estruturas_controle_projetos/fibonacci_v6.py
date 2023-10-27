def fibonacci(quantidade_numeros):
    resultado = [0, 1]

    while True:
        resultado.append(sum(resultado[-2:]))

        if len(resultado) == quantidade_numeros:
            break
    return resultado


if __name__ == '__main__':
    for valor in fibonacci(15):
        print(valor)
