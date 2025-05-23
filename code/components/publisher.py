import asyncio
import logging

from aiotaskqueue import Configuration, Publisher, task
from aiotaskqueue.broker.inmemory import InMemoryBroker
from aiotaskqueue.serialization.msgspec import MsgSpecSerializer


@task(name="send-email")
async def send_email(email: str, message: str) -> None:
    logging.info("Sending email to %s, length: %s", email, len(message))


async def main() -> None:
    configuration = Configuration(default_serialization_backend=MsgSpecSerializer())
    broker = InMemoryBroker(max_buffer_size=100)

    publisher = Publisher(broker=broker, config=configuration)
    await publisher.enqueue(
        send_email(email="email@example.com", message="Hello, World!")
    )


if __name__ == "__main__":
    asyncio.run(main())
