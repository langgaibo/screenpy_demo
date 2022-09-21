"""
Tasks related to testing various toy API apps
"""

from .add_new_device import AddNewDevice
from .delete_device import DeleteDevice
from .get_auth_token import GetAuthToken

__all__ = [
    "AddNewDevice",
    "DeleteDevice",
    "GetAuthToken",
]
