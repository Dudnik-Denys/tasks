import concurrent.futures


def get_card_number():
    for i in range(801):
        yield str(4007000000100 + i)


def do_request(card_number: str):
    return int(card_number) in range(4007000000100, 4007000000900)


# Допишите код здесь используя пул потоков, не меняйте функции get_card_number и do_request
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    [executor.submit(do_request, card) for card in get_card_number()]
