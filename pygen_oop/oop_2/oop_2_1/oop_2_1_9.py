import sys

data = [line.strip()[1:-1].split(',') for line in sys.stdin]


def validate_coordinates(x: int | float, y: int | float) -> bool:
    return -90 <= x <= 90 and -180 <= y <= 180


[print(validate_coordinates(float(num_1), float(num_2))) for num_1, num_2 in data]
