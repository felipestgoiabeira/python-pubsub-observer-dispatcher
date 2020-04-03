from functools import singledispatch

class Amarelo:
    ...

class Roxo:
    ...

class Verde:
    ...

@singledispatch
def paul(evento):
    ...

@singledispatch
def paul(evento):
    print(f'Paul se perdeu com {evento}')

@paul.register(Roxo)
def mandar_para_centauro(evento):
    print(f'Centauro recebeu a cor roxa')

@paul.register(Amarelo)
def mandar_para_fausto(evento):
    print(f'Fausto recebeu a cor amarela')

@paul.register(Verde)
def mandar_para_unicornio(evento):
    print(f'Unicornio recebeu a com Verde')

paul(Amarelo())