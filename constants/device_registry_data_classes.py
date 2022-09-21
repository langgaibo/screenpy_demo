"""
Dataclasses for api testing
"""

from dataclasses import asdict, dataclass

@dataclass(kw_only=True)
class UserData:
    """A user."""

    login: str
    password: str


@dataclass(kw_only=True)
class DeviceData:
    """A device."""
    name: str
    location: str
    type: str
    model: str
    serial_number: str

    def get_device_dict(self):
        device_dict = asdict(self)
        return device_dict
