import asyncio


async def set_future_result(value: str, delay: int | float):
    print(f'Задача начата. Установка результата {repr(value)} через {delay} секунд.')
    await asyncio.sleep(delay)
    print('Результат установлен.')
    return value


async def create_and_use_future():
    future = asyncio.ensure_future(set_future_result('Успех', 2))
    print(f'Состояние Future до выполнения: Ожидание')
    print('Задача запущена, ожидаем завершения...')
    await future
    print(f'Состояние Future после выполнения: Завершено')
    return future.result()


async def main():
    result = await create_and_use_future()
    print(f'Результат работы Future: {result}')


asyncio.run(main())
