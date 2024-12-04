import os
from datetime import datetime

dir_path = "E:\BaiduNetdiskDownload"


def get_files_1(dir: str) -> list:
    file_list = []

    for home, dirs, files in os.walk(dir):
        for file_name in files:
            file_list.append(os.path.join(home, file_name))
    return file_list


def get_files(dir: str) -> list:
    file_list = []
    if os.path.isfile(dir):
        file_list.append(dir)
        return file_list

    if os.path.isdir(dir):
        # for f in os.listdir(dir): # 简单
        for f in os.scandir(dir):  # 高效
            if os.path.isdir(f):
                file_list.append(get_files(f))
            file_list.append(os.path.join(dir, f))
    return file_list


if __name__ == "__main__":
    file_list = get_files_1(dir_path)
    for f in file_list:
        file_name = os.path.basename(f)
        last_mtime = os.path.getmtime(f)
        last_mtime_str = datetime.fromtimestamp(last_mtime)
        print(f"文件名: {file_name}, 最后更新时间: {last_mtime_str}")

        # os.utime(f) # 更新文件时间戳
 