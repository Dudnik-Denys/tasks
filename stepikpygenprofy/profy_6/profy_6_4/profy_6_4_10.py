from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

for tpl in data:
    for field, value in tpl._asdict().items():
        print(f'{field}: {value}')
    print()
