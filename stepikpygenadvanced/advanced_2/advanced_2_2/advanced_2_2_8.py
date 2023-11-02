timur, ruslan = input(), input()
rock, paper, scissors, lizard, spock = 'камень', 'бумага', 'ножницы', 'ящерица', 'Спок'


def game(timur_choice: str, ruslan_choice: str) -> str:
    results = {scissors: [paper, lizard], paper: [spock, rock], rock: [scissors, lizard], lizard: [spock, paper],
               spock: [scissors, rock]}
    if ruslan_choice in results[timur_choice]:
        return 'Тимур'
    if timur_choice in results[ruslan_choice]:
        return 'Руслан'
    return 'ничья'


print(game(timur, ruslan))
