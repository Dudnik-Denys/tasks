# получаем входящие данные
n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

# вычисляем количество на пересечениях nm, mk, nk (сколько прочитало 2 книги)
nm = n + m - t - x
mk = m + k - t - y
nk = n + k - t - z

# вычисляем новые значения для n, m, k (сколько прочитало только 1 книгу)
n = n - nk - nm - t
m = m - mk - nm - t
k = k - mk - nk - t

print(n + m + k)                            # выводим сколько прочитало только 1 книгу
print(nm + mk + nk)                         # выводим сколько прочитало 2 книги
print(a - (n + m + k + nm + mk + nk + t))   # выводим сколько не прочитало ни одной
