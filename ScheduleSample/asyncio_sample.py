import asyncio
from datetime import datetime


async def task():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # type: ignore 去掉最后3位微秒，保留毫秒
    print("Task executed at %s" % formatted_time)


async def main():
    while True:
        await task()
        await asyncio.sleep(0.03)  # 异步等待


if __name__ == "__main__":
    asyncio.run(main())
