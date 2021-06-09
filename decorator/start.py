def decorator(funcao):
    def wrapper(*arg, **kwargs):
        print('Entrou no decorator')
        print(arg)
        print(kwargs)
        funcao(*arg, **kwargs)
    return wrapper

class Hero:

    @decorator
    def metodo(self, num):
        print('Entrou na class Hero')

deku = Hero()
deku.metodo(4)