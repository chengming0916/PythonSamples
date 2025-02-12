import sched
import time
from datetime import datetime

scheduler = sched.scheduler(time.time, time.sleep)


def task():
    # timestamp = time.time()
    # local_time = time.localtime(timestamp)
    # print("Task executed at %s" % time.strftime("%Y-%m-%d %H:%M:%S", local_time))

    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # type: ignore 去掉最后3位微秒，保留毫秒
    print("Task executed at %s" % formatted_time)

    # 递归调用，实现循环
    # scheduler.enter(5, 1, task, ())
    scheduler.enter(0.03, 1, task, ())


if __name__ == "__main__":
    # 启动定时任务
    scheduler.enter(5, 1, task, ())
    scheduler.run()
