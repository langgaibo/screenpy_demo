"""
Tests of key features in the SwagLabs app!
"""

from screenpy import Actor, given, then, when
from screenpy.actions import Eventually, See
from screenpy_selenium.actions import Open
from screenpy.pacing import act, scene
from screenpy_selenium.questions import BrowserURL, Text
from screenpy.resolutions import ContainsTheText, ReadsExactly

from tasks.swaglabs import LogIntoSwagLabs
from ui.swaglabs.swaglabs_shop import PRODUCTS_HEADER, URL

email = "standard_user"
password = "secret_sauce"


@act("Functional")
@scene("Login")
def test_login(Selene: Actor) -> None:
    """Happy Path Login case."""
    given(Selene).was_able_to(LogIntoSwagLabs.using(email, password))
    then(Selene).should(
        Eventually(See.the(BrowserURL(), ReadsExactly(URL))),
        Eventually(See.the(Text.of_the(PRODUCTS_HEADER), ContainsTheText("PRODUCTS"))),
    )
