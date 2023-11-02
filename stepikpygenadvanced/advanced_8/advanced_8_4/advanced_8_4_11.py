fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
new = sorted([elem for elem in fruits], reverse=True)
[print(elem) for elem in new]
