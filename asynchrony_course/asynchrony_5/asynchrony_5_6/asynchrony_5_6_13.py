import asyncio


# Корутина для отправки запроса.
async def equipment_request(request: str):
    await asyncio.sleep(1)
    return f'{request[:4]} is Ok!'


# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [equipment_request(data) for data in equipment_list]
    results = await asyncio.gather(*tasks)
    waiting_time = query_time()
    print(f'На отправку {len(equipment_list)} запросов потребовалось {waiting_time} секунд!')
