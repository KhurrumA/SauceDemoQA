import pytest
from selenium import webdriver
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Result(pass/fail)
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

    driver.quit()
