string = input().split()
piece_size = int(input())
size = int(len(string) / piece_size)
start = 0
end = piece_size
new = []
extra = len(string) % piece_size

for x in range(size):
    new.append(string[start:end])
    start += piece_size
    end += piece_size

if extra != 0:
    new.append(string[-extra:])

print(new)


# def chunked(symbols, n):
#     result = []
#     for i in range(0, len(symbols), n):
#         result.append(symbols[i:i + n])
#     return result
#
# symbols = input().split()
# n = int(input())
#
# print(chunked(symbols, n))
