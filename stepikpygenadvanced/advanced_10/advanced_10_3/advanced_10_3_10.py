lst = list(range(1, 16))
squares = [i * i for i in lst]
result = {key: value for key, value in zip(lst, squares)}
print(result)

# result = {i : i ** 2 for i in range(1,16)}
