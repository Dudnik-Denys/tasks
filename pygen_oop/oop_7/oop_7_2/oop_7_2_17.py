from datetime import date


class WeatherWarning:
    @staticmethod
    def rain():
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow():
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature():
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, dt: date):
        print(f'{dt.strftime("%d.%m.%Y")}')
        super().rain()

    def snow(self, dt: date):
        print(f'{dt.strftime("%d.%m.%Y")}')
        super().snow()

    def low_temperature(self, dt: date):
        print(f'{dt.strftime("%d.%m.%Y")}')
        super().low_temperature()
