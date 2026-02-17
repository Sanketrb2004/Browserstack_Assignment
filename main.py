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
#         "json": {
#             "text": text
#         }
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "X-RapidAPI-Key": "89885d7e38msh6b56401b8d73a72p1c0c81jsn4a7159c76f75",
#         "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
#     }

#     response = requests.post(url, json=payload, headers=headers, timeout=20)
#     return response.json()["trans"]["text"]


# # ===========================================================

# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     wait = WebDriverWait(driver, 20)

#     driver.get("https://elpais.com/opinion/")

#     # Wait until at least some articles load
#     wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "article h2 a")) >= 5)

#     # ⭐ GET ALL ARTICLES FIRST
#     all_articles = driver.find_elements(By.CSS_SELECTOR, "article h2 a")

#     # ⭐ TAKE FIRST 5 REAL TITLES FROM TOP
#     articles = []
#     for a in all_articles:
#         title = a.text.strip()
#         if title and title.strip() != "":

#             articles.append(a)
#         if len(articles) == 5:
#             break

#     if not os.path.exists("images"):
#         os.makedirs("images")

#     translated_titles = []

#     print("\nProcessing First 5 Articles...\n")

#     for i, article in enumerate(articles, start=1):

#         title = article.text.strip()
#         link = article.get_attribute("href")

#         print(f"\nArticle {i}: {title}")

#         # TRANSLATE
#         try:
#             translated = translate_text(title)
#             translated_titles.append(translated)
#             print("Translated Title:", translated)
#         except Exception as e:
#             print("Translation Failed:", e)

#         # OPEN ARTICLE PAGE
#         driver.get(link)
#         time.sleep(3)

#         # CONTENT EXTRACTION
#         paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")
#         content = " ".join([p.text for p in paragraphs[:5]])

#         print("Content Preview:", content[:200], "...")

#         # IMAGE DOWNLOAD
#         try:
#             image = driver.find_element(By.CSS_SELECTOR, "figure img")
#             image_url = image.get_attribute("src")

#             img = requests.get(image_url, timeout=20).content
#             with open(f"images/article_{i}.jpg", "wb") as f:
#                 f.write(img)

#             print("Image downloaded")

#         except:
#             print("No image found")

#         driver.back()
#         time.sleep(2)

#     print("\nAll Translated Titles:\n", translated_titles)

#     input("\nPress Enter to close browser...")

# except Exception as e:
#     print("Error:", e)

# finally:
#     driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
import os

# ================= GOOGLE TRANSLATE FUNCTION =================

def translate_text(text):

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

        # Handle both string and dict API response
        if isinstance(trans, dict):
            return trans.get("text", "")
        return trans

    except:
        return ""

# ===========================================================

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

try:

    # STEP 1 — Open Opinion Page
    driver.get("https://elpais.com/opinion/")

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "article")) > 5)

    # STEP 2 — Extract FIRST 5 REAL ARTICLES (TOP TO BOTTOM)
    article_blocks = driver.find_elements(By.CSS_SELECTOR, "article")

    articles_data = []

    for block in article_blocks:
        try:
            title_el = block.find_element(By.CSS_SELECTOR, "h2 a")
            title = title_el.text.strip()
            link = title_el.get_attribute("href")

            if title and link:
                articles_data.append((title, link))

        except:
            continue

        if len(articles_data) == 5:
            break

    # STEP 3 — Prepare Image Folder
    if not os.path.exists("images"):
        os.makedirs("images")

    translated_titles = []

    print("\nProcessing First 5 Articles...\n")

    # STEP 4 — Process Each Article
    for i, (title, link) in enumerate(articles_data, start=1):

        print(f"\nArticle {i}: {title}")

        # Translate Title
        translated = translate_text(title)
        translated_titles.append(translated)
        print("Translated Title:", translated)

        # Open Article Page
        driver.get(link)
        time.sleep(3)

        # Extract Spanish Content
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")
        content = " ".join([p.text for p in paragraphs[:5]])
        print("Content Preview:", content[:200], "...")

        # Download Cover Image
        try:
            img = driver.find_element(By.CSS_SELECTOR, "figure img")
            img_url = img.get_attribute("src")

            img_data = requests.get(img_url, timeout=20).content
            with open(f"images/article_{i}.jpg", "wb") as f:
                f.write(img_data)

            print("Image downloaded")

        except:
            print("No image found")

        # Go Back to Opinion Page
        driver.get("https://elpais.com/opinion/")
        time.sleep(2)

    print("\nTranslated Titles:\n", translated_titles)

    input("\nPress Enter to close browser...")

finally:
    driver.quit()
