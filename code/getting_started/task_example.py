from aiotaskqueue import task


@task(name="task-name")
async def my_task() -> None:
    pass
