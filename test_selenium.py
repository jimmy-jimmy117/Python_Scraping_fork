from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import random
import time
from selenium.webdriver.common.by import By


option = Options()
option.add_argument("--headless")

driver = webdriver.Chrome(options=option)
driver.get("https://www.google.co.jp/")

# 検索フィールドの取得
query = driver.find_element(by=By.NAME, value="q")

# 検索文字列を入力
query.send_keys("python")

# 3秒待つ
time.sleep(3)

# 検索ボタンをクリック
button = driver.find_element(by=By.NAME, value="btnK")
button.click()

# 3秒待つ
time.sleep(3)

# 検索結果ページのURLを取得
search_results = driver.find_elements_by_css_selector("div.r a")
search_result_urls = [link.get_attribute("href") for link in search_results]

# 検索結果の中からランダムに1つのページを選択し、そのページに移動
selected_url = random.choice(search_result_urls)
driver.get(selected_url)

# ページの読み込みを待つ
time.sleep(3)  # 3秒待つ（必要に応じて調整）

# ページのテキストを取得
page_text = driver.find_element_by_tag_name("body").text

# 検索文字の出現回数をカウント
word_count = page_text.count(search_word)

# 結果を出力
print(f"ページ '{selected_url}' における '{search_word}' の出現回数: {word_count}")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

ll = [x for x in soup.text.split(" ") if len(x) > 0]
for elem in ll:
    print(elem)
