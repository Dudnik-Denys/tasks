emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

k = []

for key, value in emails.items():
    for i in range(len(value)):
        k.append(value[i] + '@' + key)

print(*sorted(k), sep='\n')

# print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')
