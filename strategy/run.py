from .src import Guerreiro, LutaArco, LutaEspada, Curar, Mago

cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(LutaArco(9))
curandeiro = Guerreiro(Curar(4))
mago = Guerreiro(Mago(10))

cavaleiro.acao()
cavaleiro.attributos()

arqueiro.acao()
arqueiro.attributos()
curandeiro.attributos()
mago.attributos()

''' Principio da inversão de dependencias '''