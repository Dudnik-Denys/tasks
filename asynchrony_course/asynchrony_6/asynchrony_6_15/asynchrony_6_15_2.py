import asyncio
import random

open_ports = []


async def scan_port(host: str, port: int) -> None:
    status = random.choice([True, False])
    await asyncio.sleep(random.randint(1, 5))
    print(f'Порт {port} на адресе {host} {"открыт" if status else "закрыт"}')
    if status:
        open_ports.append(port)


async def scan_range(address: str, start_port: int, end_port: int) -> None:
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    async with asyncio.TaskGroup() as group:
        [group.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)]

    print(f'Открытые порты на адресе {address}: {open_ports}' if open_ports else f'Открытых портов на адресе '
                                                                                 f'{address} не найдено')


asyncio.run(scan_range('192.168.0.1', 80, 85))
