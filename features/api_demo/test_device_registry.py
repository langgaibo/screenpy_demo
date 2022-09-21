"""
Tests of various API endpoint functionality
"""

import pytest

from screenpy import Actor, and_, given, then, when
from screenpy.actions import See
from screenpy.resolutions import EqualTo, IsEqualTo, IsNot, ContainsTheEntry, ContainsTheKey
from screenpy_requests.actions import (
    AddHeader,
    SendAPIRequest,
    SendGETRequest,
    SendDELETERequest,
    SendOPTIONSRequest,
    SendPATCHRequest,
    SendPOSTRequest,
    SendPUTRequest,
)
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse,
)

from constants.device_registry_constants import (
    Pythonista,
    Engineer,
    PorchLight,
    Thermostat,
    Fridge,
)
from constants.device_registry_data_classes import DeviceData
from tasks.api_demo import GetAuthToken
from ui.api_demo.device_manager import AUTH_ENDPOINT, DEVICE_ENDPOINT

def test_invalid_auth_credentials(Arlong: Actor) -> None:
    """Attempting to auth with invalid credentials should return an error."""
    when(Arlong).attempts_to(
        SendGETRequest.to(AUTH_ENDPOINT)
        .with_(auth=(Pythonista.login, "farts"))
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(401)),
        See.the(BodyOfTheLastResponse(), ContainsTheEntry(message="Invalid credentials")),
    )


def test_post_nothing(Arlong: Actor) -> None:
    """Making an empty POST call should result in a 400 error."""
    given(Arlong).was_able_to(GetAuthToken.using("pythonista", "I<3testing"))
    when(Arlong).attempts_to(SendPOSTRequest.to(DEVICE_ENDPOINT))
    then(Arlong).should(See.the(StatusCodeOfTheLastResponse(), IsEqualTo(400)))

def test_add_device(Arlong: Actor) -> None:
    """Making a properly formatted POST call to add a device should work."""

    given(Arlong).was_able_to(
        GetAuthToken.using(Pythonista.login, Pythonista.password),
    )
    when(Arlong).attempts_to(
        SendPOSTRequest.to(DEVICE_ENDPOINT).with_(json=PorchLight.get_device_dict()),
    )
    and_(Arlong).attempts_to(
        SendGETRequest.to(DEVICE_ENDPOINT),
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse(), ContainsTheKey("devices")),
    )

# # Example of a single test iterating through parameters via parametrize
# @pytest.mark.parametrize("action", ["DELETE", "GET", "PATCH", "POST", "PUT"])
# def test_actions(action: str, Arlong: Actor) -> None:
#     """All HTTP verb requests respond with 200s."""
#     when(Arlong).attempts_to(SendAPIRequest(action, f"{BASE_URL}/{action.lower()}"))

#     then(Arlong).should(See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)))


# def test_base_64_decoder(Arlong: Actor) -> None:
#     """Base64 decoder decodes!"""
#     test_string = "SW4gYSBiaW5nIGNvdW50cnkgeW91ciBzZWFyY2ggaXMgbGlua2VkIHRvIHlvdQ=="

#     when(Arlong).attempts_to(SendGETRequest.to(f"{BASE64_URL}/{test_string}"))

#     then(Arlong).should(
#         See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
#         See.the(
#             BodyOfTheLastResponse(),
#             ReadsExactly("In a bing country your search is linked to you")
#         )
#     )
