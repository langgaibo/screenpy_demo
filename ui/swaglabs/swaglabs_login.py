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
