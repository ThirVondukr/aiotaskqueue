from aiotaskqueue import TaskRouter
from aiotaskqueue.extensions.retry import Retry

router = TaskRouter()


@router.task(
    name="task-name",
    markers=[Retry(max_retries=3)],
)
async def my_task() -> None:
    pass
