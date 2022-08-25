"""
Elements on the SwagLabs Login screen!
"""

from screenpy_selenium import Target

LOGIN_FIELD = Target.the("Username field").located_by(
    '#user-name'
)
PASSWORD_FIELD = Target.the("Password field").located_by(
    '#password'
)
LOGIN_BUTTON = Target.the("Login Button").located_by(
    '#login-button'
)
URL = 'https://www.saucedemo.com/'

# URL = 'http://the-internet.herokuapp.com/dynamic_controls'

# TROUBLE_BOX = Target.the("checkbox").located_by(
#     '//input[@type="checkbox"]'
# )
# TEXT_FIELD = "asdf"
# WAITING_TEXT = Target.the('"Wait for it..." text').located_by(
#     '//div[contains(text(), "Wait for it")]'
# )

# REMOVE_BUTTON = Target.the("Remove button").located_by(
#     '//button[contains(text(), "Remove")]'
# )

# ADD_BUTTON = Target.the("Add button").located_by(
#     '//button[contains(text(), "Add")]'
# )

# DISABLE_BUTTON = Target.the("Disable Button").located_by(
#     '//button[contains(text(), "Disable")]'
# )
# ENABLE_BUTTON = Target.the("Enable Button").located_by(
#     '//button[contains(text(), "Enable")]'
# )

