import asyncio


async def async_operation():
    print('Начало асинхронной операции.')
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print('Асинхронная операция была отменена в процессе выполнения.')
        raise
    else:
        print('Асинхронная операция успешно завершилась.')


async def main():
    print('Главная корутина запущена.')
    future = asyncio.ensure_future(async_operation())
    await asyncio.sleep(0.1)
    print('Попытка отмены Future.')
    future.cancel()
    try:
        await future
        print('Результат Future:', future.result())
    except asyncio.CancelledError:
        print('Обработка исключения: Future был отменен.')
        print('Проверка: Future был отменен.' if future.cancelled() else 'Проверка: Future не был отменен.')
    finally:
        print('Главная корутина завершена.')


asyncio.run(main())
