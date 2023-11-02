ru = 'АаВСсЕеНКМОоРрТХху'
en = 'AaBCcEeHKMOoPpTXxy'
symbols = [ord(input()) for _ in range(3)]

if all(map(lambda x: True if x > 1000 else False, symbols)):
    print('ru')
elif all(map(lambda x: True if x < 1000 else False, symbols)):
    print('en')
else:
    print('mix')


# def russian_or_english(symbols):
#     languages = {'ru' if s in 'АаВСсЕеНКМОоРрТХху' else 'en' for s in symbols}
#     if len(languages) == 1:
#         return languages.pop()
#     return 'mix'
#
#
# letters = [input() for _ in range(3)]
# print(russian_or_english(letters))
