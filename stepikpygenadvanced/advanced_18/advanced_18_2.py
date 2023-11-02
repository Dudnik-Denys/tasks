with open('ledger.txt', 'r', encoding='utf-8') as file:
    print('$' + str(sum([int(price.strip('$')) for price in file.readlines()])))
