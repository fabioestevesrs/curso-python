def fibonacci(quantidade_numeros, sequencia=(0, 1)):
    return sequencia if len(sequencia) == quantidade_numeros else \
        fibonacci(quantidade_numeros, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for valor in fibonacci(20):
        print(valor)
