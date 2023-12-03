word1 = sorted([char for char in sorted(input().lower().strip('.,:;!?-').replace(' ', '')) if char not in '.,:;!?-'])
word2 = sorted([char for char in sorted(input().lower().strip('.,:;!?-').replace(' ', '')) if char not in '.,:;!?-'])
print(['YES', 'NO'][word1 != word2])
