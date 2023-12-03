prices = ['$50', '$40', '$10']
print(list(int(price.strip('$')) for price in prices))