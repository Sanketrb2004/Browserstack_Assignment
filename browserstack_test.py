from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading

USERNAME = "sanketbauskar_vibxzj"
ACCESS_KEY = "3PNtG423aCNmX4TxZxvY"

URL = "https://elpais.com/opinion/"


def run_test(capabilities):

    options = Options()

    for key, value in capabilities.items():
        options.set_capability(key, value)

    BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    # ⭐ Create Device Display Name
    if "deviceName" in capabilities:
        device_label = capabilities["deviceName"]
    else:
        device_label = f'{capabilities.get("browserName")} {capabilities.get("os")}'

    print(f"\n[INFO] Starting test on: {device_label}")

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get(URL)

        wait = WebDriverWait(driver, 20)

        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article h2 a"))
        )

        all_articles = driver.find_elements(By.CSS_SELECTOR, "article h2 a")
        first_five = all_articles[:5]

        print(f"[SUCCESS] {device_label} → Found {len(first_five)} Articles (First 5 Verified)")

    except Exception as e:
        print(f"[ERROR] {device_label} → {e}")

    finally:
        driver.quit()



browsers = [

    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "osVersion": "10"},
    {"browserName": "Edge", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Safari", "browserVersion": "latest", "os": "OS X", "osVersion": "Monterey"},
    {"deviceName": "Samsung Galaxy S22", "realMobile": "true", "osVersion": "12.0"},
    {"deviceName": "iPhone 13", "realMobile": "true", "osVersion": "15"}

]

threads = []

print("\n[INFO] Running Parallel BrowserStack Tests...\n")

for browser in browsers:
    t = threading.Thread(target=run_test, args=(browser,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\n[INFO] All Tests Completed")
