import asyncio
import itertools
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

combinations = list(itertools.product(shapes, colors, actions))


async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    tasks = [asyncio.create_task(launch_firework(sh, clr, act)) for sh, clr, act in combinations]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
