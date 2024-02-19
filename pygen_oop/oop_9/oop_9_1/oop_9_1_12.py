from copy import copy


class Selfie:
    def __init__(self):
        self.statements = []

    def save_state(self):
        temp = Selfie()
        temp.__dict__ = copy(self.__dict__)
        self.statements.append(temp)

    def recover_state(self, index):
        if index not in range(len(self.statements)):
            return self
        self.statements[index].statements = self.statements[:index]
        return self.statements[index]

    def n_states(self):
        return len(self.statements)
