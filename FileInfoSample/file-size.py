import os

dir_path = "F:\Music"


def get_files(dir: str) -> list:
    file_list = []
    if os.path.isfile(dir):
        file_list.append(dir)
        return file_list

    if os.path.isdir(dir):
        for f in os.listdir(dir):
            if os.path.isdir(f):
                file_list.append(get_files(f))
            file_list.append(os.path.join(dir, f))
    return file_list


def get_size_str(size: int) -> str:
    if size < 1024:
        return f"{round(size, 2)} Byte"
    if size < 1024 * 1024:
        return f"{round(size / 1024, 2)} KB"
    if size < 1024 * 1024 * 1024:
        return f"{round(size / (1024 * 1024), 2)} MB"

    pass


if __name__ == "__main__":
    file_list = get_files(dir_path)
    for f in file_list:
        file_name = os.path.basename(f)
        file_size = os.path.getsize(f)
        file_size_str = get_size_str(file_size)
        print(f"文件名: {file_name}, 大小: {file_size_str}")
