import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    run_mode = os.getenv("RUN_MODE", "local")

    if run_mode == "browserstack":
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

        url = f"https://{username}:{access_key}@hub.browserstack.com/wd/hub"

        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")

        options.set_capability("bstack:options", {
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Testathon Automation",
        })

        return webdriver.Remote(command_executor=url, options=options)

    # LOCAL RUN (default)
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)