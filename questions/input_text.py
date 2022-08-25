"""
Investigate the contents of a free text input field.
"""

# from typing import List, Union

from screenpy import Actor
from screenpy.pacing import beat

from screenpy_selenium import Target

class InputText:
    """
    
    """

    @staticmethod
    def of_the(target: Target) -> "InputText":
        """Target the element to extract the text from."""
        return InputText(target=target)
    
    of = of_the

    def describe(self) -> str:
        """Describe the Question."""
        return f"The current input text in the {self.target}"
    
    @beat("{} reads the input text from the {target}.")
    def answered_by(self, the_actor: Actor) -> str:
        """Direct the Actor to read off the input text of the element."""
        scrutinized_text_field = self.target.found_by(the_actor)
        # Thanks to https://stackoverflow.com/a/55844014 for the 'get_property' solution!
        text_content = scrutinized_text_field.get_property('value')
        return text_content

    def __init__(self, target: Target) -> None:
        self.target = target
