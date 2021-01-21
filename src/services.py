import logging
import time
import random

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# https://gist.github.com/fijimunkii/952acac988f2d25bef7e0284bc63c406
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
]


def get_rendered_html(*, url: str) -> str:
    logger.info(f"URL: {url}")

    options = Options()
    options.headless = True

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.accept_untrusted_certs = True
    firefox_profile.set_preference("browser.download.downloadDir", "/tmp")
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    firefox_profile.set_preference(
        "general.useragent.override", random.choice(user_agents)
    )

    logger.info("Prepared Firefox profile")

    browser = webdriver.Firefox(
        options=options, firefox_profile=firefox_profile, service_log_path=None
    )
    logger.info("Initialized Firefox browser")

    browser.get(url)

    logger.info("Waiting for page to fully load")
    time.sleep(5)

    inner_html = browser.execute_script(
        "return document.getElementsByTagName('html')[0].innerHTML"
    )

    browser.quit()

    return "<html>" + inner_html + "</html>"
