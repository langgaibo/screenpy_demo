"""
Dataclasses for api testing
"""
from datetime import date
from dataclasses import asdict, dataclass

@dataclass(kw_only=True)
class UserData:
    """A user."""
    login: str
    password: str

@dataclass(kw_only=True)
class CustomerData:
    """A customer."""
    first_name: str
    last_name: str
    dob: str # expect format YYYY-MM-DD
    address: str
    login: str
    password: str
    
    def get_age(self) -> int:
        """return the customer's age."""
        today = date.today()
        birth_year, month, day = (int(time_) for time_ in self.dob.split("-"))
        birthday = date(today.year, month, day)
        age = today.year - birth_year
        if birthday > today:
            age -= 1
        return age


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
