from aiotaskqueue import task


@task(name="test-task")
async def noop_task() -> None:
    pass


@task(name="task-with-params")
async def task_with_params(a: int, b: str) -> None:
    pass
