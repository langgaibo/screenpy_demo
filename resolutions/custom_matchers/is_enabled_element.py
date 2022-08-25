"""
A matcher that matches an enabled element. For example:

    assert_that(driver.find_element_by_type("input"), is_enabled_element())
"""

from typing import Optional

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from selenium.webdriver.remote.webelement import WebElement


class IsEnabledElement(BaseMatcher[Optional[WebElement]]):
    """
    Matches an element whose ``is_enabled`` method returns True.
    """

    def _matches(self, item: Optional[WebElement]) -> bool:
        if item is None:
            return False
        return item.is_enabled()

    def describe_to(self, description: Description) -> None:
        """Describe the passing case."""
        description.append_text("the element is enabled")

    def describe_match(
        self, item: Optional[WebElement], match_description: Description
    ) -> None:
        match_description.append_text("it was enabled")

    def describe_mismatch(
        self, item: Optional[WebElement], mismatch_description: Description
    ) -> None:
        """Describe the failing case."""
        if item is None:
            mismatch_description.append_text("was not even present")
            return
        mismatch_description.append_text("was not enabled")


def is_enabled_element() -> IsEnabledElement:
    """This matcher matches any element that is enabled."""
    return IsEnabledElement()
