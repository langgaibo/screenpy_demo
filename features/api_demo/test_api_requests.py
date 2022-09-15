"""
Tests of the Request Bin website
"""

import pytest

from screenpy import Actor, then, when
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ReadsExactly
from screenpy_requests.actions import SendAPIRequest, SendGETRequest
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse,
)

from ui.api_demo.http_bin import (
    BASE_URL,
    BASIC_AUTH_URL,
    BEARER_AUTH_URL,
    SET_COOKIES_URL,
    BASE64_URL,
)

@pytest.mark.parametrize("action", ["DELETE", "GET", "PATCH", "POST", "PUT"])
def test_actions(action: str, Arlong: Actor) -> None:
    """All HTTP verb requests respond with 200s."""
    when(Arlong).attempts_to(SendAPIRequest(action, f"{BASE_URL}/{action.lower()}"))

    then(Arlong).should(See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)))


def test_base_64_decoder(Arlong: Actor) -> None:
    """Base64 decoder decodes!"""
    test_string = "SW4gYSBiaW5nIGNvdW50cnkgeW91ciBzZWFyY2ggaXMgbGlua2VkIHRvIHlvdQ=="

    when(Arlong).attempts_to(SendGETRequest.to(f"{BASE64_URL}/{test_string}"))

    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(
            BodyOfTheLastResponse(),
            ReadsExactly("In a bing country your search is linked to you")
        )
    )
