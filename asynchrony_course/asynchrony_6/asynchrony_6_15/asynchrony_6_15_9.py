import asyncio

passengers = [
    {"Name": "John", "Age": 25, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sarah", "Age": 32, "Speed": 6, "Job": "Doctor"},
    {"Name": "Mike", "Age": 28, "Speed": 4, "Job": "Teacher"},
    {"Name": "Emma", "Age": 30, "Speed": 3, "Job": "Nurse"},
    {"Name": "Robert", "Age": 45, "Speed": 7, "Job": "Lawyer"},
    {"Name": "Olivia", "Age": 27, "Speed": 3, "Job": "Architect"},
    {"Name": "Charlie", "Age": 35, "Speed": 4, "Job": "Chef"},
    {"Name": "Sophia", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Jacob", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Grace", "Age": 31, "Speed": 6, "Job": "Designer"},
    {"Name": "William", "Age": 34, "Speed": 7, "Job": "Writer"},
    {"Name": "Chloe", "Age": 26, "Speed": 3, "Job": "Journalist"},
    {"Name": "Lucas", "Age": 33, "Speed": 4, "Job": "Pilot"},
    {"Name": "Ella", "Age": 28, "Speed": 4, "Job": "Artist"},
    {"Name": "Ethan", "Age": 37, "Speed": 6, "Job": "Actor"},
    {"Name": "Ava", "Age": 30, "Speed": 4, "Job": "Dancer"},
    {"Name": "Noah", "Age": 32, "Speed": 1, "Job": "Musician"},
    {"Name": "Isabella", "Age": 33, "Speed": 6, "Job": "Singer"},
    {"Name": "Liam", "Age": 31, "Speed": 4, "Job": "Director"},
    {"Name": "Mia", "Age": 29, "Speed": 3, "Job": "Producer"},
    {"Name": "Alexander", "Age": 35, "Speed": 8, "Job": "Engineer"},
    {"Name": "Sophie", "Age": 32, "Speed": 4, "Job": "Doctor"},
    {"Name": "Benjamin", "Age": 28, "Speed": 3, "Job": "Teacher"},
    {"Name": "Emily", "Age": 30, "Speed": 4, "Job": "Nurse"},
    {"Name": "James", "Age": 45, "Speed": 6, "Job": "Lawyer"},
    {"Name": "Amelia", "Age": 27, "Speed": 4, "Job": "Architect"},
    {"Name": "Henry", "Age": 35, "Speed": 3, "Job": "Chef"},
    {"Name": "Jessica", "Age": 40, "Speed": 2, "Job": "Scientist"},
    {"Name": "John", "Age": 25, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sarah", "Age": 32, "Speed": 6, "Job": "Doctor"},
    {"Name": "Mike", "Age": 28, "Speed": 4, "Job": "Teacher"},
    {"Name": "Emma", "Age": 30, "Speed": 3, "Job": "Nurse"},
    {"Name": "Robert", "Age": 45, "Speed": 7, "Job": "Lawyer"},
    {"Name": "Olivia", "Age": 27, "Speed": 3, "Job": "Architect"},
    {"Name": "Charlie", "Age": 35, "Speed": 4, "Job": "Chef"},
    {"Name": "Sophia", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Jacob", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Grace", "Age": 31, "Speed": 6, "Job": "Designer"},
    {"Name": "William", "Age": 34, "Speed": 7, "Job": "Writer"},
    {"Name": "Chloe", "Age": 26, "Speed": 3, "Job": "Journalist"},
    {"Name": "Lucas", "Age": 33, "Speed": 4, "Job": "Pilot"},
    {"Name": "Ella", "Age": 28, "Speed": 8, "Job": "Artist"},
    {"Name": "Ethan", "Age": 37, "Speed": 6, "Job": "Actor"},
    {"Name": "Ava", "Age": 30, "Speed": 4, "Job": "Dancer"},
    {"Name": "Noah", "Age": 32, "Speed": 2, "Job": "Musician"},
    {"Name": "Isabella", "Age": 33, "Speed": 6, "Job": "Singer"},
    {"Name": "Liam", "Age": 31, "Speed": 4, "Job": "Director"},
    {"Name": "Mia", "Age": 29, "Speed": 3, "Job": "Producer"},
    {"Name": "Alexander", "Age": 35, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sophie", "Age": 32, "Speed": 4, "Job": "Doctor"},
    {"Name": "Benjamin", "Age": 28, "Speed": 3, "Job": "Teacher"},
    {"Name": "Emily", "Age": 30, "Speed": 4, "Job": "Nurse"},
    {"Name": "James", "Age": 45, "Speed": 6, "Job": "Lawyer"},
    {"Name": "Amelia", "Age": 27, "Speed": 4, "Job": "Architect"},
    {"Name": "Henry", "Age": 35, "Speed": 3, "Job": "Chef"},
    {"Name": "Jessica", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Daniel", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Antonio", "Age": 70, "Speed": 1, "Job": "Pensioner"},
    {"Name": "Sinty", "Age": 69, "Speed": 2, "Job": "Pensioner"},
    {"Name": "Avame", "Age": 18, "Speed": 9, "Job": "Programmer"},
    ]


async def boarding(passenger):
    try:
        await asyncio.sleep(passenger["Speed"])
        print(f'{passenger["Name"]} сел в автобус.')
    except asyncio.CancelledError:
        print(f'{passenger["Name"]} {passenger["Job"]} не успел/а вовремя сесть в автобус.')


async def main():
    tasks = [asyncio.create_task(boarding(passenger)) for passenger in passengers]
    completed, pending = await asyncio.wait(tasks, timeout=5)
    [task.cancel() for task in pending]


if __name__ == "__main__":
    asyncio.run(main())
