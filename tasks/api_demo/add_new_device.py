"""
Add a new device to the device registry, storing the ID for later use if needed.
"""

from screenpy import Actor
from screenpy.actions import MakeNote
from screenpy.pacing import beat
from screenpy_requests.actions import SendPOSTRequest
from screenpy_requests.questions import BodyOfTheLastResponse
from test_data.device_registry_data_classes import DeviceData
from ui.api_demo.device_manager import DEVICE_ENDPOINT


class AddNewDevice:
    """Add a new device to the device registry.

    Accepts a DeviceData dataclass instance.

    This task adds a Director's Note of the device ID, which can be accessed after
    storage under "added device id"
    
    Examples::
    
        the_actor.attempts_to(AddNewDevice(PorchLight))
    """

    @beat("{} adds a new device to the registry.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to add a new device."""
        the_actor.attempts_to(
            SendPOSTRequest.to(DEVICE_ENDPOINT)
            .with_(json=self.device.get_device_dict()),
        )
        device_id = BodyOfTheLastResponse().answered_by(the_actor)["id"]
        the_actor.attempts_to(
            MakeNote.of_the(device_id).as_("added device id")
        )
    
    def __init__(self, device: DeviceData) -> None:
        self.device = device
