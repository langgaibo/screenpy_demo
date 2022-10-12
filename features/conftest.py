"""
Configurations and fixtures for Pytest
"""

import os
from datetime import datetime
from typing import Any, Generator

import pytest
from dotenv import load_dotenv
from screenpy import Actor
from screenpy_requests.abilities import MakeAPIRequests
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import SaveConsoleLog, SaveScreenshot
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


CHROME_OPTIONS = Options()
CHROME_OPTIONS.set_capability("goog:loggingPrefs", {"browser": "ALL"})

load_dotenv('.env')

@pytest.fixture(scope="function")
def Selene() -> Generator:
    """Create an actor who can surf the information superhighway"""
    driver = Chrome(options=CHROME_OPTIONS)
    the_actor = Actor.named("Selene").who_can(BrowseTheWeb.using(driver))
    yield the_actor
    # capture a screenshot at the end of the test
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H%M%S")
    ss_path = os.path.join("debug", f"screenshot-{timestamp}.png")
    the_actor.attempts_to(
        SaveScreenshot.as_(ss_path)
    )
    # capture the console log at the end of the test
    js_path = os.path.join("debug", f"console-log-{timestamp}.txt")
    the_actor.attempts_to(
        SaveConsoleLog.as_(js_path)
    )
    the_actor.exit()

@pytest.fixture(scope="function")
def Arlong() -> Generator:
    """Create an actor who can make API requests."""
    the_actor = Actor.named("Arlong").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit()
