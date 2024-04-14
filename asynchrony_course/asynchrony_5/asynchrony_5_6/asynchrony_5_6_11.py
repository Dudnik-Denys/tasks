import asyncio

# Полный десериализованый JSON вшит в задачу
books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    ]


async def check_book(book):
    return book if not book["Наличие на полке"] else None


async def main():
    tasks = [asyncio.create_task(check_book(item)) for item in books_json]
    results = await asyncio.gather(*tasks)
    [print(f'{result["Порядковый номер"]}: {result["Автор"]}: {result["Название"]} ({result["Год издания"]})') for
     result in results if result]


asyncio.run(main())
