import asyncio

addresses = {0: '192.168.0.3', 1: '192.168.0.1', 2: '192.168.0.2', 3: '192.168.0.4', 4: '192.168.0.5'}


async def worker(ip_id, ip, event):
    print(f'Датчик {ip_id} IP-адрес {ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {ip_id} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')


async def manager(evnet):
    await asyncio.sleep(1)
    evnet.set()
    print('Датчики зафиксировали движение')


async def main():
    event = asyncio.Event()
    tasks = [asyncio.ensure_future(worker(key, value, event)) for key, value in addresses.items()]
    tasks.append(asyncio.create_task(manager(event)))
    await asyncio.gather(*tasks)

asyncio.run(main())
