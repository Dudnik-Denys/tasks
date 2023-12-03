import pickle
import sys

data = [line.strip() for line in sys.stdin]

with open(data[0], 'rb') as file:
    function = pickle.load(file)
    print(function(*data[1:]))
