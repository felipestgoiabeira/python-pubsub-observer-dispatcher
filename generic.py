class generic:
    def __init__(self, default):
        self.funcs = []
        self.default = default
    
    def when(self, pred):
        def add(func):
            self.funcs.append( (pred, func) )
            return func
        return add

    def __call__(self, *args, **kwargs):
        for pred, func in self.funcs:
            try:
                match = pred(*args, **kwargs)
            except Exception:
                match = False
            if match:
                return func(*args, **kwargs)
            return self.default(*args, **kwargs)


@generic
def paul(evento):
    print(f'{evento}')

@paul.when(lambda evento: evento['cor'] == 'amarelo')
def amarelo(evento):
    print(evento)
        