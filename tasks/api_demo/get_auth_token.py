"""
Obtain and add a bearer auth token to the session header.
"""

from screenpy import Actor
from screenpy.pacing import beat
from screenpy.exceptions import UnableToAct
from screenpy_requests.actions import SendGETRequest, AddHeader
from screenpy_requests.questions import BodyOfTheLastResponse
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
    def using(username: str, password: str) -> "GetAuthToken":
        return GetAuthToken(username, password)

    @beat("{} obtains an auth token for the device registry.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to get an auth token."""
        if not self.username or not self.password:
            raise UnableToAct(
                "Need valid username and password to obtain auth token."
            )
        
        the_actor.attempts_to(
            SendGETRequest.to(AUTH_ENDPOINT).with_(auth=(self.username, self.password))
        )
        bearer_token = BodyOfTheLastResponse().answered_by(the_actor)["token"]
        the_actor.attempts_to(AddHeader(Authorization=f"Bearer {bearer_token}"))

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
