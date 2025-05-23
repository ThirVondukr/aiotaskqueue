import asyncio

from aiotaskqueue import Configuration, Publisher, task
from aiotaskqueue.broker.inmemory import InMemoryBroker
from aiotaskqueue.serialization.msgspec import MsgSpecSerializer


@task(name="task")
async def notify_user(user_id: int, message: str) -> None:
    pass


async def main() -> None:
    broker = InMemoryBroker(max_buffer_size=100)
    configuration = Configuration(default_serialization_backend=MsgSpecSerializer())

    publisher = Publisher(broker=broker, config=configuration)

    await publisher.enqueue(
        notify_user(
            user_id=42,
            message="Your notification!",
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
