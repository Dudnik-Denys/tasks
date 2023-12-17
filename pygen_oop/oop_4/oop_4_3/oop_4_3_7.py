class Gun:
    index = 0

    def shoot(self):
        print(['pif', 'paf'][self.index % 2])
        self.index += 1
