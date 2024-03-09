import concurrent.futures


# Напишите функцию post_worker
def post_worker(future):
    try:
        result = future.result()
    except Exception as err:
        print(err)
    else:
        print(f'{result} saved')


# Создайте пул потоков и запустите выполнение целевой задачи worker, после получения результатов
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(worker, source) for source in sources]
    # запустите функцию пост обработчика результата. Если при получении результата возбуждаются исключения,
    # выведите сообщение в консоль.
    [future.add_done_callback(post_worker) for future in futures]
