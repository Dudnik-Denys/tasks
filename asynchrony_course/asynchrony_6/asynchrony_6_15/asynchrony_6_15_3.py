import asyncio
import random

data = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}


async def scan_port(address: str, port: int) -> int | None:
    status = False
    await asyncio.sleep(1)

    if random.randint(0, 100) == 1:
        status = True
        print(f'Port {port} on {address} is open')

    if status:
        return port
    return None


async def scan_range(address: str, start_port: int, end_port: int) -> tuple:
    open_ports = []
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [asyncio.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    [open_ports.append(result) for result in results if result is not None]
    return address, open_ports


async def main(dct) -> None:
    tasks = [asyncio.create_task(scan_range(port, diapason[0], diapason[1])) for port, diapason in dct.items()]
    results = await asyncio.gather(*tasks)
    [print(f'Всего найдено открытых портов {len(task[1])} {task[1]} для ip: {task[0]}') for task in results if task[1]]


asyncio.run(main(data))
