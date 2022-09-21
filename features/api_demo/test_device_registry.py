"""
Tests against Automation Panda's toy Device Registry app https://github.com/AutomationPanda/device-registry
"""

from screenpy import Actor, and_, given, then, when
from screenpy.actions import See
from screenpy.resolutions import EqualTo, IsEqualTo, IsNot, ContainsTheEntry, ContainsTheKey
from screenpy_requests.actions import (
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
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse(), ContainsTheEntry(name="Front Porch Light")),
    )
