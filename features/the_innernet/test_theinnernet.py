"""
Tests of the Dynamic Controls page... on... The Internet!
"""

from screenpy import Actor, given, when, then
from screenpy.actions import Eventually, See
from screenpy_selenium.actions import Click, Enter, Open, Wait
from screenpy_selenium.questions import Element
from screenpy.resolutions import ContainsTheText, IsNot
from screenpy_selenium.resolutions import Visible
from questions import InputText
from ui.the_innernet.dynamic_controls import (
    CHECKBOX,
    TEXT_FIELD,
    WAITING_TEXT,
    REMOVE_BUTTON,
    ADD_BUTTON,
    DISABLE_BUTTON,
    ENABLE_BUTTON,
    URL
)

def test_remove_checkbox(Selene: Actor) -> None:
    """Test that the checkbox is removed when the remove button is clicked."""
    given(Selene).was_able_to(Open.their_browser_on(URL))
    when(Selene).attempts_to(
        Wait.for_the(CHECKBOX).to_appear(),
        Click.on_the(REMOVE_BUTTON),
        Wait.for_the(WAITING_TEXT).to_appear(),
        Wait.for_the(WAITING_TEXT).to_disappear(),
    )
    then(Selene).should(
        Eventually(See.the(Element(CHECKBOX), IsNot(Visible())))
    )

def test_enable_text_field(Selene: Actor) -> None:
    """Test that the text field is enabled by the Enable button, by entering text."""

    test_text = "I am entering text!"

    given(Selene).was_able_to(Open.their_browser_on(URL))
    when(Selene).attempts_to(
        Wait.for_the(TEXT_FIELD).to_appear(),
        Click.on_the(ENABLE_BUTTON),
        Wait.for_the(WAITING_TEXT).to_appear(),
        Wait.for_the(WAITING_TEXT).to_disappear(),
        Eventually(Enter.the_text(test_text).into_the(TEXT_FIELD)),
    )
    then(Selene).should(
        See.the(InputText.of_the(TEXT_FIELD), ContainsTheText(test_text)),
    )
