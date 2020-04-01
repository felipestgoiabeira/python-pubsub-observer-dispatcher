class Observador:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        """Fazer o que quiser com a msg"""
        print(f'|{self.nome} recebeu| {mensagem} ')

class Passaro:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)
    
    def notificar_observadores(self, msg):
        for observador in self.observadores:
            observador.atualizar(msg)

eduardo = Observador('Felipe')
bruno = Observador('Bruno')
fabricio = Observador('Fabricio')

passaro = Passaro()
passaro.adicionar_observador(eduardo)
passaro.adicionar_observador(bruno)
passaro.adicionar_observador(fabricio)

passaro.notificar_observadores('Estou voando')

