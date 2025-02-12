import time
import schedule
from datetime import datetime


def task():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # type: ignore 去掉最后3位微秒，保留毫秒
    print("Task executed at %s" % formatted_time)


if __name__ == "__main__":
    schedule.every(5).seconds.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)  # 避免CPU占用过高
