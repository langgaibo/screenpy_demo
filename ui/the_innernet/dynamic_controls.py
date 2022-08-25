"""
Elements on the internet!
"""

from screenpy_selenium import Target

CHECKBOX = Target.the("checkbox").located_by(
    '//input[@type="checkbox"]'
)
TEXT_FIELD = Target.the("text field").located_by(
    '//input[@type="text"]'
)
WAITING_TEXT = Target.the('"Wait for it..." text').located_by(
    '//div[contains(text(), "Wait for it")]'
)

REMOVE_BUTTON = Target.the("Remove button").located_by(
    '//button[contains(text(), "Remove")]'
)

ADD_BUTTON = Target.the("Add button").located_by(
    '//button[contains(text(), "Add")]'
)

DISABLE_BUTTON = Target.the("Disable Button").located_by(
    '//button[contains(text(), "Disable")]'
)
ENABLE_BUTTON = Target.the("Enable Button").located_by(
    '//button[contains(text(), "Enable")]'
)
URL = 'http://the-internet.herokuapp.com/dynamic_controls'
