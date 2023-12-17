from collections import namedtuple


class Postman:
    def __init__(self):
        self.delivery_data = []
        self.Address = namedtuple('Address', ['street', 'house', 'apartment'])

    def add_delivery(self, street: str, house: int, apartment: int):
        self.delivery_data.append(self.Address(street, house, apartment))

    def get_houses_for_street(self, street: str) -> list:
        return list({address.house: None for address in self.delivery_data if address.street == street})

    def get_flats_for_house(self, street: str, house: int) -> list:
        return list({address.apartment: None for address in self.delivery_data if address.street == street
                    and address.house == house})
