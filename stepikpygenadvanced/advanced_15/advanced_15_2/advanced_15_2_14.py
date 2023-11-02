def print_products(*args):
    products = [product for product in args if isinstance(product, str) and len(product) > 0]
    if len(products) == 0:
        print('Нет продуктов')
    else:
        for i in range(len(products)):
            print(f'{i + 1}) {products[i]}')
