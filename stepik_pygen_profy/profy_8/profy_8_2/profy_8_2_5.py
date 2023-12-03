def traffic(n):
    if n > 0:
        print('Не парковаться')
        return traffic(n - 1)
