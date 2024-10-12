import requests
from bs4 import BeautifulSoup


# 下载章节内容
def downLoad(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find_all('h2', class_="chapter-title")
        title = title[0].text + ".txt"
        content = soup.find_all('div', class_="article")
        for e in content:
            with open(title, "a", encoding="utf-8") as f:
                print("【+】已下载保存为：" + title)
                f.write(str(e.text))
    except:
        pass

# 开始爬取
try:
    Num = input("【+】请输入你要爬取多少章节的小说：")
    Num = int(Num)
    rooturl = "https://www.qimao.com/shuku/149774-3172"

    if Num == 1:
        downLoad("https://www.qimao.com/shuku/149774-316193/")
    else:
        downLoad("https://www.qimao.com/shuku/149774-316193/")
        for i in range(71, 70 + Num):
            chapter_url = f"{rooturl}{i}/"
            r = requests.get(chapter_url, timeout=10)
            if r.status_code == 200:
                downLoad(chapter_url)
            else:
                print(f"【-】小说章节无法下载: {chapter_url}")

except ValueError:
    print("【-】请输入有效的整数。")
except Exception as e:
    print(f"【-】发生错误: {e}")