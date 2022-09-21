"""
Delete a device from the device registry.
"""

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_requests.actions import SendDELETERequest
from ui.api_demo.device_manager import DEVICE_ENDPOINT


class DeleteDevice:
    """Deletes a device with the supplied device ID value from the device registry.

    Examples::
    
        the_actor.attempts_to(DeleteDevice(noted_under("added device id")))
    """
    
    @beat("{} deletes a device.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to delete a device."""
        
        the_actor.attempts_to(
            SendDELETERequest.to(f"{DEVICE_ENDPOINT}/{self.device_id}")
        )
    
    def __init__(self, device_id: str) -> None:
        self.device_id = device_id
