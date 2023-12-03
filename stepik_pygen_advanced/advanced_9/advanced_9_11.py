n = int(input())
m = int(input())
lst1 = [input() for _ in range(n)]
lst2 = [input() for _ in range(m)]
lst1len = len(lst1) - len(set(lst1))
lst2len = len(lst2) - len(set(lst2))
total, cmn = set(lst1) | set(lst2), set(lst1) & set(lst2)
size = len(total - cmn) - lst1len - lst2len
print(['NO', size][size > 0])
