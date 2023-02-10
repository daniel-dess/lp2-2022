class ControleBonificacao():
    def __init__(self):
        self._total = 0

    def registra(self, f):
        try:
            self._total += f.get_bonifica()
        except AttributeError as ae:
            print(f'Estagiário não é Funcionario.')

    @property
    def total(self):
        return self._total