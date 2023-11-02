from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_value = lambda: [(key, value) for key, value in data.items() if value == min(data.values())]
data.max_value = lambda: [(key, value) for key, value in data.items() if value == max(data.values())]
