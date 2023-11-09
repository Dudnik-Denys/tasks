func = input()
segment = list(map(int, input().split()))
execute = lambda x: eval(func)
results = [execute(num) for num in range(segment[0], segment[1] + 1)]

print(f'Минимальное значение функции {func} на отрезке [{segment[0]}; {segment[1]}] равно {min(results)}\n'
      f'Максимальное значение функции {func} на отрезке [{segment[0]}; {segment[1]}] равно {max(results)}')
