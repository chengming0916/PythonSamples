import sys
import time
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 其实网页
start_url = "https://www.bqgui.cc"

novel_id = "1604"

# 请求网页
response = requests.get(start_url + "/book/" + novel_id, headers=headers)

# 解析网页
soup = BeautifulSoup(response.text, "html.parser")

# 获取内容列表
a_tags = soup.find("div", class_="listmain").find_all("a")

novel_name = soup.find("div", class_="info").find("h1").text

save_path = f"./{novel_name}.txt"

chapters = {}

with open(save_path, "w", encoding="utf-8") as f:
    for a in a_tags:
        try:
            href = str(a.get("href"))

            if href.startswith("javascript"):
                continue
            chapter_response = requests.get(
                start_url + a.get("href"),
                headers=headers,
            )
            chapter_soup = BeautifulSoup(chapter_response.text, "html.parser")
            title = chapter_soup.find("h1", class_="wap_none").text
            content = chapter_soup.find("div", id="chaptercontent").text

            # 删除章节内容中的“请收藏本站”
            endIndex = content.find("请收藏本站")
            content = content[:endIndex]

            print("下载章节 - ", title)

            f.write(title + "\n" + content + "\n")
        except Exception as e:
            print("下载章节失败 - ", a.get("href"))
