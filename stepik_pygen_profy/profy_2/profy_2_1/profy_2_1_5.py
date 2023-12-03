def hide_card(card_number: str) -> str:
    card_number = '************' + card_number.replace(' ', '')[-4:]
    return card_number
