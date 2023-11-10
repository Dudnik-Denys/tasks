from datetime import date


def date_formatter(country_code: str) -> callable:
    codes = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def result(input_date: date) -> str:
        return date.strftime(input_date, codes[country_code])
    return result
