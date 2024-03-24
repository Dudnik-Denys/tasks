import asyncio


async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x


async def main():
    results = [asyncio.create_task(compute_square(i)) for i in range(10)]
    completed, pending = await asyncio.wait(results)
    for task in completed:
        print(f"Результат: {task.result()}")


asyncio.run(main())
