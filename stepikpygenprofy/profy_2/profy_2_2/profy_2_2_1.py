path = [int(input()) for _ in range(3)]
first_path = path[0] * 2 + path[1] * 2
second_path = sum(path)
third_path = path[0] * 2 + path[2] * 2
fourth_path = path[1] * 2 + path[2] * 2


print(min(first_path, second_path, third_path, fourth_path))
