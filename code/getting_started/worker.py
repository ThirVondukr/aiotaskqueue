import asyncio

from aiotaskqueue import Configuration, TaskRouter
from aiotaskqueue.broker.redis import RedisBroker
from aiotaskqueue.serialization.msgspec import MsgSpecSerializer
from aiotaskqueue.worker import AsyncWorker
from redis.asyncio import Redis

router = TaskRouter()


@router.task("my-task")
async def my_task() -> None:
    pass


async def main() -> None:
    broker = RedisBroker(redis=Redis(), consumer_name="your-consumer-name")
    configuration = Configuration(default_serialization_backend=MsgSpecSerializer())

    worker = AsyncWorker(
        tasks=router,
        broker=broker,
        configuration=configuration,
        concurrency=100,
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
