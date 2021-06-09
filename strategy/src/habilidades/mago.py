from .interfaces import Ihabilidade

class Mago(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print('Feitiços e magia')

    def nivel_atributo(self):
        print('Nivel de uso magico: {}'.format(self.nivel))