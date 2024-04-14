import asyncio


async def publish_post(text: str) -> None:
    print(f"Пост опубликован: {text}")


async def notify_subscribers(subs: list) -> None:
    [print(f"Уведомление отправлено {sub}") for sub in subs]


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await asyncio.gather(publish_post(post_text), notify_subscribers(subscribers))


# запускаем асинхронную функцию main()
asyncio.run(main())
