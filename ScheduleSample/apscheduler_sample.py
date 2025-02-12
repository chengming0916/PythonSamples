from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def task():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # type: ignore 去掉最后3位微秒，保留毫秒
    print("Task executed at %s" % formatted_time)


if __name__ == "__main__":
    # 创建调度器
    scheduler = BlockingScheduler()

    # 关联任务，每5秒执行一次
    scheduler.add_job(task, "interval", seconds=5)
    scheduler.start()
