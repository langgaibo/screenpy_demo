"""
Tests against Automation Panda's toy Device Registry app,
found here: https://github.com/AutomationPanda/device-registry
"""

from screenpy import Actor, and_, given, then, when
from screenpy.actions import See
from screenpy.directions import noted_under
from screenpy.resolutions import (
    IsEqualTo,
    ContainsTheEntry,
    ContainsTheText,
)
from screenpy_requests.actions import (
    SendGETRequest,
    SendPOSTRequest,
)
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    StatusCodeOfTheLastResponse,
)

from constants.device_registry_constants import (
    Pythonista,
    PorchLight,
    Thermostat,
)
from constants.device_registry_data_classes import DeviceData
from tasks.api_demo import AddNewDevice, DeleteDevice, GetAuthToken
from ui.api_demo.device_manager import AUTH_ENDPOINT, DEVICE_ENDPOINT

def test_invalid_auth_credentials(Arlong: Actor) -> None:
    """Attempting to auth with invalid credentials should return an error."""
    when(Arlong).attempts_to(
        SendGETRequest.to(AUTH_ENDPOINT)
        .with_(auth=(Pythonista.login, "farts"))
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(401)),
        See.the(
            BodyOfTheLastResponse(), ContainsTheEntry(message="Invalid credentials")
        ),
    )


def test_post_nothing(Arlong: Actor) -> None:
    """Making an empty POST call should result in a 400 error."""
    given(Arlong).was_able_to(GetAuthToken.using(Pythonista.login, Pythonista.password))
    when(Arlong).attempts_to(SendPOSTRequest.to(DEVICE_ENDPOINT))
    then(Arlong).should(See.the(StatusCodeOfTheLastResponse(), IsEqualTo(400)))


def test_add_device(Arlong: Actor) -> None:
    """Making a properly formatted POST call to add a device should work."""
    given(Arlong).was_able_to(GetAuthToken.using(Pythonista.login, Pythonista.password))
    when(Arlong).attempts_to(
        AddNewDevice(PorchLight),
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
        See.the(BodyOfTheLastResponse(), ContainsTheEntry(name="Front Porch Light")),
    )
    # For now, explicitly delete the device, since we aren't wiping the DB.
    and_(Arlong).should(DeleteDevice(noted_under("added device id")))

def test_missing_device_field(Arlong: Actor) -> None:
    """Attempting to add a device with missing fields should result in an error."""
    nameless_light = {
        # intentionally leave out name field
        "location": "13th floor",
        "type": "light",
        "model": "Noside",
        "serial_number": "-1"
    }
    given(Arlong).was_able_to(GetAuthToken.using(Pythonista.login, Pythonista.password))
    when(Arlong).attempts_to(
        SendPOSTRequest.to(DEVICE_ENDPOINT).with_(json=nameless_light)
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(400)),
        See.the(
            BodyOfTheLastResponse(),
            ContainsTheEntry(
                message="request body has missing fields: name"
            ),
        ),
    )

def test_invalid_type_value(Arlong: Actor) -> None:
    """Invalid data type should return an error."""
    broken_serial_device = Thermostat.get_device_dict()
    broken_serial_device["serial_number"] = {}
    given(Arlong).was_able_to(GetAuthToken.using(Pythonista.login, Pythonista.password))
    when(Arlong).attempts_to(
        SendPOSTRequest.to(DEVICE_ENDPOINT).with_(json=broken_serial_device)
    )
    then(Arlong).should(
        See.the(StatusCodeOfTheLastResponse(), IsEqualTo(500)),
        See.the(BodyOfTheLastResponse(), ContainsTheText("internal error")),
    )
