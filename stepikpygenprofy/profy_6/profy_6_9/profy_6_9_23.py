from collections import ChainMap

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
data = tuple(input().split(','))


def total_sum(order: tuple) -> int:
    total = 0
    for ingredient in order:
        total += ingredients[ingredient]
    return total


def products_count(order: tuple) -> dict:
    counter = {}
    for ingredient in sorted(order):
        counter[ingredient] = counter.get(ingredient, 0) + 1
    return counter


total_count = total_sum(data)
products = products_count(data)
final_sum = f'ИТОГ: {total_count}р'
max_len_item = len(max(products.keys(), key=len))

[print(f'{item.ljust(max_len_item)} x {value}') for item, value in products.items()]
print('-' * ((max_len_item) + 4))
print(f'ИТОГ: {total_count}р')
