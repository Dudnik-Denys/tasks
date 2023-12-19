class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.num_of_pets() > 0 else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.num_of_pets() > 0 else None
