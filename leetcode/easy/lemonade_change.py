def lemonade_change(bills: list[int]) -> bool:
    money = {5: 0,
             10: 0}

    for bill in bills:
        if bill == 5:
            money[bill] += 1
        elif bill == 10:
            if money[5] >= 1:
                money[5] -= 1
                money[bill] += 1
            else:
                return False
        else:
            if money[5] >= 1 and money[10] >= 1:
                money[10] -= 1
                money[5] -= 1
            elif money[5] >= 3:
                money[5] -= 3
            else:
                return False
    return True
