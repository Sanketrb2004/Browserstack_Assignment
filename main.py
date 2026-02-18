
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# import requests
# import time
# import os

# # ================= GOOGLE TRANSLATE FUNCTION =================

# def translate_text(text):

#     url = "https://google-translate113.p.rapidapi.com/api/v1/translator/json"

#     payload = {
#         "from": "es",
#         "to": "en",
#         "json": {"text": text}
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "X-RapidAPI-Key": "89885d7e38msh6b56401b8d73a72p1c0c81jsn4a7159c76f75",
#         "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
#     }

#     try:
#         r = requests.post(url, json=payload, headers=headers, timeout=20)
#         data = r.json()

#         trans = data.get("trans", "")

#         # Handle both string and dict API response
#         if isinstance(trans, dict):
#             return trans.get("text", "")
#         return trans

#     except:
#         return ""

# # ===========================================================

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# wait = WebDriverWait(driver, 20)

# try:

#     # STEP 1 — Open Opinion Page
#     driver.get("https://elpais.com/opinion/")

#     wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "article")) > 5)

#     # STEP 2 — Extract FIRST 5 REAL ARTICLES (TOP TO BOTTOM)
#     article_blocks = driver.find_elements(By.CSS_SELECTOR, "article")

#     articles_data = []

#     for block in article_blocks:
#         try:
#             title_el = block.find_element(By.CSS_SELECTOR, "h2 a")
#             title = title_el.text.strip()
#             link = title_el.get_attribute("href")

#             if title and link:
#                 articles_data.append((title, link))

#         except:
#             continue

#         if len(articles_data) == 5:
#             break

#     # STEP 3 — Prepare Image Folder
#     if not os.path.exists("images"):
#         os.makedirs("images")

#     translated_titles = []

#     print("\nProcessing First 5 Articles...\n")

#     # STEP 4 — Process Each Article
#     for i, (title, link) in enumerate(articles_data, start=1):

#         print(f"\nArticle {i}: {title}")

#         # Translate Title
#         translated = translate_text(title)
#         translated_titles.append(translated)
#         print("Translated Title:", translated)

#         # Open Article Page
#         driver.get(link)
#         time.sleep(3)

#         # Extract Spanish Content
#         paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")
#         content = " ".join([p.text for p in paragraphs[:5]])
#         print("Content Preview:", content[:200], "...")

#         # Download Cover Image
#         try:
#             img = driver.find_element(By.CSS_SELECTOR, "figure img")
#             img_url = img.get_attribute("src")

#             img_data = requests.get(img_url, timeout=20).content
#             with open(f"images/article_{i}.jpg", "wb") as f:
#                 f.write(img_data)

#             print("Image downloaded")

#         except:
#             print("No image found")
#         # Go Back to Opinion Page
#         driver.get("https://elpais.com/opinion/")
#         time.sleep(2)
#     print("\nTranslated Titles:\n", translated_titles)

#     # ================= WORD REPETITION ANALYSIS =================
#     from collections import Counter

#     all_words = []

#     for title in translated_titles:
#         if title:   # ⭐ Safety check (avoid empty strings)
#             words = title.lower().split()
#             all_words.extend(words)

#     word_count = Counter(all_words)

#     print("\nWords repeated more than twice:\n")

#     found = False   # ⭐ Industry pattern flag

#     for word, count in word_count.items():
#         if count > 2:
#             print(f"{word} -> {count}")
#             found = True

#     if not found:
#         print("No words repeated more than twice.")

#     # ===========================================================

#     input("\nPress Enter to close browser...")

# finally:
#     driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import os

# ================= GOOGLE TRANSLATE FUNCTION =================

def translate_text(text):

    print("[INFO] Translating title...")

    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/json"

    payload = {
        "from": "es",
        "to": "en",
        "json": {"text": text}
    }

    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "89885d7e38msh6b56401b8d73a72p1c0c81jsn4a7159c76f75",
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=20)
        data = r.json()
        trans = data.get("trans", "")

        if isinstance(trans, dict):
            return trans.get("text", "")
        return trans

    except:
        print("[WARN] Translation failed")
        return ""

# ===========================================================

print("[INFO] Launching browser...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

try:

    print("[INFO] Opening Opinion section...")
    driver.get("https://elpais.com/opinion/")

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "article")) > 5)

    print("[INFO] Opinion section loaded successfully.")

    # ⭐ GUARANTEED FIRST 5 REAL ARTICLES
    articles_data = []

    print("[INFO] Extracting first 5 article titles...")

    while len(articles_data) < 5:

        article_blocks = driver.find_elements(By.CSS_SELECTOR, "article")

        for block in article_blocks:
            try:
                title_el = block.find_element(By.CSS_SELECTOR, "h2 a")
                title = title_el.text.strip()
                link = title_el.get_attribute("href")

                if title and link and (title, link) not in articles_data:
                    print(f"[INFO] Found article title: {title}")
                    articles_data.append((title, link))

            except:
                continue

            if len(articles_data) == 5:
                break

        if len(articles_data) < 5:
            print("[INFO] Waiting for more articles to load...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    print(f"[INFO] Total Articles Collected: {len(articles_data)}")

    if not os.path.exists("images"):
        os.makedirs("images")

    translated_titles = []

    print("\n[INFO] Processing Articles...\n")

    for i, (title, link) in enumerate(articles_data, start=1):

        print(f"\n[INFO] Processing Article {i}")
        print(f"[INFO] Spanish Title: {title}")

        translated = translate_text(title)
        translated_titles.append(translated)
        print(f"[INFO] Translated Title: {translated}")

        print("[INFO] Opening article page...")
        driver.get(link)

        # ⭐ SAFE FAST WAIT
        try:
            wait.until(lambda d:
                len(d.find_elements(By.CSS_SELECTOR, "article")) > 0 or
                len(d.find_elements(By.TAG_NAME, "p")) > 0
            )
        except:
            print("[WARN] Article content slow, continuing...")

        paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")
        content = " ".join([p.text for p in paragraphs[:5]])

        print("[INFO] Content extracted successfully.")

        try:
            print("[INFO] Downloading article image...")
            img = driver.find_element(By.CSS_SELECTOR, "figure img")
            img_url = img.get_attribute("src")

            img_data = requests.get(img_url, timeout=20).content
            with open(f"images/article_{i}.jpg", "wb") as f:
                f.write(img_data)

            print("[INFO] Image downloaded successfully.")

        except:
            print("[WARN] No image found.")

        print("[INFO] Returning to Opinion section...")
        driver.get("https://elpais.com/opinion/")
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "article")) > 5)

    print("\n[INFO] All Translated Titles:\n", translated_titles)

    # ================= WORD REPETITION ANALYSIS =================
    from collections import Counter

    print("\n[INFO] Performing word repetition analysis...")

    all_words = []

    for title in translated_titles:
        if title:
            all_words.extend(title.lower().split())

    word_count = Counter(all_words)

    print("\nWords repeated more than twice:\n")

    found = False
    for word, count in word_count.items():
        if count > 2:
            print(f"{word} -> {count}")
            found = True

    if not found:
        print("No words repeated more than twice.")

    print("\n[INFO] Script execution completed successfully.")

    input("\nPress Enter to close browser...")

finally:
    print("[INFO] Closing browser...")
    driver.quit()

