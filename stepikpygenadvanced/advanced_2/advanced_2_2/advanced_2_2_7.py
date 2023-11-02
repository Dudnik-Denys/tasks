timur, ruslan = input(), input()
rock = 'камень'
paper = 'бумага'
scissors = 'ножницы'


def rock_paper_scissors(timur_choice: str, ruslan_choice: str) -> str:
    results = {rock: scissors, paper: rock, scissors: paper}

    if results[timur_choice] == ruslan_choice:
        return 'Тимур'
    if results[ruslan_choice] == timur_choice:
        return 'Руслан'

    return 'ничья'


print(rock_paper_scissors(timur, ruslan))
