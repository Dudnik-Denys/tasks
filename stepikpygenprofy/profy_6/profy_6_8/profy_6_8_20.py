from collections import Counter


def print_bar_chart(data: str | list[str], mark: str):
    counter = Counter(data)
    [print(f'{key.ljust(len(max(counter.keys(), key=len)))} |{mark * value}') for key, value in sorted(counter.items(), key=lambda x: x[1], reverse=True)]
