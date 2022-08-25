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


# """
# Tests of the Dynamic Controls page... on... The Internet!
# """

# from screenpy import Actor, given, when, then
# from screenpy.actions import Eventually, See
# from screenpy_selenium.actions import Click, Enter, Open, Wait
# from screenpy_selenium.questions import TheElement
# from screenpy_selenium.resolutions import IsVisible, IsInvisible
# from ui.swaglabs.swaglabs_login import (
#     TROUBLE_BOX,
#     TEXT_FIELD,
#     WAITING_TEXT,
#     REMOVE_BUTTON,
#     ADD_BUTTON,
#     DISABLE_BUTTON,
#     ENABLE_BUTTON,
#     URL
# )

# def test_remove_TROUBLE_BOX(Selene: Actor) -> None:
#     """Test that the TROUBLE_BOX is removed when the remove button is clicked."""
#     given(Selene).was_able_to(Open.their_browser_on(URL))
#     when(Selene).attempts_to(
#         Wait.for_the(TROUBLE_BOX).to_appear(),
#         Click.on_the(REMOVE_BUTTON),
#         Wait.for_the(WAITING_TEXT).to_appear(),
#         Wait.for_the(WAITING_TEXT).to_disappear(),
#     )
#     then(Selene).should(
#         Eventually(See(TheElement(TROUBLE_BOX), IsInvisible))
#     )
