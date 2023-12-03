from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

bag_weight = int(input())
bag_price = -1
bag_items = None

for i in range(1, 11):
    for comb in combinations(items, i):
        comb_price = sum(item.price for item in comb)
        comb_weight = sum(item.mass for item in comb)
        if comb_price > bag_price and comb_weight <= bag_weight:
            bag_items = comb
            bag_price = comb_price

if bag_items:
    for item in sorted(bag_items):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')
