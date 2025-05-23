def funcao(func ,*args, **kwargs):
    def interna():
        return func(*args, **kwargs)
    return interna

if __name__ == '__main__':
    soma = funcao(sum, [10, 20, 30])
    print(soma())