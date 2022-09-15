"""
Fixtures for the API demo suite
"""

from typing import Generator

import pytest

from screenpy import Actor
from screenpy_requests.abilities import MakeAPIRequests

@pytest.fixture
def Arlong() -> Generator:
    """An actor who can make API requests."""
    the_actor = Actor.named("Arlong").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit_stage_left()
