from aiotaskqueue import TaskRouter

router = TaskRouter()


@router.task(name="task-name")
async def my_task() -> None:
    pass
