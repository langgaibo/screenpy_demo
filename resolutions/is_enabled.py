"""
Matches against an enabled WebElement.
"""

from screenpy.resolutions.base_resolution import BaseResolution

from .custom_matchers import is_enabled_element
from .custom_matchers.is_enabled_element import IsEnabledElement


class IsEnabled(BaseResolution):
    """Match on an enabled element.

    Examples::

        the_actor.should(See.the(Element(TEXT_BOX), IsEnabled()))
    """

    matcher: IsEnabledElement
    line = "enabled"
    matcher_function = is_enabled_element

    def __init__(self) -> None:  # pylint: disable=useless-super-delegation
        super().__init__()
