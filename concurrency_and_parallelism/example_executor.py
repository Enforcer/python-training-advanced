import asyncio
import time


def heavy_task(seconds: int) -> None:
    # this is not compatible with asyncio
    # so it would block!
    time.sleep(seconds)


async def main() -> None:
    # BAD - run non-cooperative code
    heavy_task(1)
    heavy_task(2)
    # GOOD - delegate non-cooperative code to executor
    loop = asyncio.get_running_loop()
    task_1 = loop.run_in_executor(None, heavy_task, 1)
    task_2 = loop.run_in_executor(None, heavy_task, 2)
    await asyncio.wait([task_1, task_2])


if __name__ == "__main__":
    start = time.monotonic()
    asyncio.run(main(), debug=True)
    print(f"Took {time.monotonic() - start}s")
