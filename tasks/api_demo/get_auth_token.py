"""
Obtain and add a bearer auth token to the session header.
"""

from screenpy import Actor
from screenpy.pacing import beat
from screenpy.exceptions import UnableToAct
from screenpy_requests.actions import SendGETRequest, AddHeader
from screenpy_requests.questions import BodyOfTheLastResponse
from test_data.device_registry_data_classes import UserData
from ui.api_demo.device_manager import AUTH_ENDPOINT

class GetAuthToken:
    """Obtain and add the bearer auth token for the device registry app,
    and add it to the session header, allowing subsequent API calls that
    require Authentication to be executed.

    Examples::

        the_actor.attempts_to(
            GetAuthToken.using(username, password)
        )
    """

    @staticmethod
    def as_(user: UserData) -> "GetAuthToken":
        return GetAuthToken(user)

    @beat("{} obtains an auth token for the device registry.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to get an auth token."""
        if not self.user:
            raise UnableToAct(
                "Need valid instance of a UserData dataclass."
            )
        
        the_actor.attempts_to(
            SendGETRequest.to(AUTH_ENDPOINT).with_(auth=(self.username, self.password))
        )
        bearer_token = BodyOfTheLastResponse().answered_by(the_actor)["token"]
        the_actor.attempts_to(AddHeader(Authorization=f"Bearer {bearer_token}"))

    def __init__(self, user: UserData) -> None:
        self.user = user
        self.username = self.user.login
        self.password = self.user.password
