import threading
from datetime import datetime


def task():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # type: ignore 去掉最后3位微秒，保留毫秒
    print("Task executed at %s" % formatted_time)

    threading.Timer(5, task).start()


if __name__ == "__main__":
    task()
