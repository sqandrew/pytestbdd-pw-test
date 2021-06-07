import pytest
from slugify import slugify
from pathlib import Path

#@pytest.fixture(scope="session")
#def browser_type(playwright, browser_name: str):
    #return getattr(playwright, 'chromium')


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"{slugify(item.nodeid)}.png"))