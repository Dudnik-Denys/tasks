from datetime import date


class DateFormatter:
    _FORMATS = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, user_date: date):
        return user_date.strftime(DateFormatter._FORMATS[self.country_code])
