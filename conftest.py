import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()

    # options.add_argument("--headless")

    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, "
        "like Gecko) Version/9.0.2 Safari/601.3.9")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    url = 'https://www.amazon.com'
    driver.get(url)

    yield driver
