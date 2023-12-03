cnt = int(input())
refs = [input() for elem in range(cnt)]

for ref in refs:
    index = 0
    a_index = ref.find('a')
    if a_index != -1:
        index += a_index
        n_1_index = ref[index:].find('n')
        if n_1_index != -1:
            index += n_1_index
            t_index = ref[index:].find('t')
            if t_index != -1:
                index += t_index
                o_index = ref[index:].find('o')
                if o_index != -1:
                    index += o_index
                    n_2_index = ref[index:].find('n')
                    if n_2_index != -1:
                        print(refs.index(ref) + 1, end=' ')

# n = int(input())
# for i in range(n):
#     seq = ["a", "n", "t", "o", "n"]
#     s = list(input())
#
#     while seq and s:  # пока у нас непустые список из букв строки и список слова "anton"
#         if seq[0] == s[0]:  # если буквы равны, то вырываем и там, и там
#             seq.pop(0)
#             s.pop(0)
#         else:  # иначе вырываем только из списка букв строки
#             s.pop(0)
#
#     # если список букв слова "anton" пустой, значит вырвали все буквы,
#     # значит в строке встретились все эти буквы в нужном нам порядке
#     if not seq:
#         print(i + 1, end=" ")
