class Money:
    def __init__(self, money):
        self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        if isinstance(mn, Money):
            self.__money += mn.__money

    @staticmethod
    def check_money(money):
        return type(money) == int and money >= 0

    def set_money(self, money):
        self.__money = money if self.check_money(money) else self.__money
