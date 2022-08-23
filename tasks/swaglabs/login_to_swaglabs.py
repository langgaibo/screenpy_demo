"""
Log the user into SwagLabs
"""

from screenpy import Actor
from screenpy.exceptions import UnableToAct
from screenpy.actions import Eventually
from screenpy_selenium.actions import Click, Enter, Open, Wait
from screenpy.pacing import beat

from ui.swaglabs.swaglabs_login import (
    LOGIN_FIELD,
    PASSWORD_FIELD,
    LOGIN_BUTTON,
    URL,
)

class LogIntoSwagLabs:
    """Log into the Labs... with Swag!

    Examples::

        the_actor.attempts_to(LogInToSwagLabs.using(USERNAME, PASSWORD))
    """

    @staticmethod
    def using(username: str, password: str) -> "LogIntoSwagLabs":
        """Set which username and password to use."""
        return LogIntoSwagLabs(username, password)
    
    @beat("{} logs into SwagLabs.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to log into SwagLabs."""
        if not self.username or not self.password:
            raise UnableToAct("Need valid username and password to log in.")

        the_actor.attempts_to(
            Open.their_browser_on(URL),
            Wait.for_the(LOGIN_FIELD).to_appear(),
            Enter.the_text(self.username).into_the(LOGIN_FIELD),
            Enter.the_password(self.password).into_the(PASSWORD_FIELD),
            Click.on_the(LOGIN_BUTTON),
        )

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
