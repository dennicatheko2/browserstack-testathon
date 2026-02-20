import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
import pytest_html
from dotenv import load_dotenv
import os

load_dotenv()  

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot = f"reports/screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot)
            report.extra = getattr(report, "extra", [])
            report.extra.append(screenshot)

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_html(report, data):
    if hasattr(report, "extra"):
        for extra in report.extra:
            if extra.endswith(".png"):
                data.append(
                    f'<img src="../screenshots/{os.path.basename(extra)}" '
                    f'style="width:300px;" />'
                )