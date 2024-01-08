class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {str(self.cpu.fr)}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: ' + "; ".join(f"{x.name} - {x.volume}" for x in self.mem_slots)]


mb = MotherBoard('Z590', CPU('Intel', 3.8), Memory('GIGABYTE', '16GB'), Memory('GIGABYTE', '16GB'))
