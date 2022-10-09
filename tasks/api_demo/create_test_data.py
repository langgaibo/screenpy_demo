"""
Task to create some test data using the Data Factory endpoint.
"""

import json

from screenpy import Actor, Director
from screenpy.actions import See
from screenpy_requests.actions import SendPOSTRequest
from screenpy.pacing import beat
from screenpy_requests.questions import BodyOfTheLastResponse, StatusCodeOfTheLastResponse
from screenpy.resolutions import ContainsTheKey, IsEqualTo

from ui.api_demo.device_manager import DATA_FACTORY_URL

from ._base_create_test_data import _BaseCreateTestData


class CreateTestData(_BaseCreateTestData):
    """Create test data using the backend factories.

    Examples::

        the_actor.attempts_to(
            CreateTestData.using("customers.tests.factories.CustomerCartFactory"),
        )

        the_actor.attempts_to(
            CreateTestData.using("customers.tests.factories.CustomerCartFactory")
            .with_data(
                {"customer_id": CUSTOMER_PK}
            ),
        )

        the_actor.attempts_to(
            CreateTestData.using("customers.tests.factories.CustomerCartFactory")
            .with_data(
                {"customer_id": CUSTOMER_PK, "item__pk": ITEM_PK}
            ).and_receipt("discount_applied", {"item.discount": "coupon"}),
        )
    """

    @staticmethod
    def using(factory_class: str) -> "CreateTestData":
        """Set the factory class to use, as a dotted-path string."""
        return CreateTestData(factory_class)

    def with_data(self, data: dict) -> "CreateTestData":
        """Set the data to pass as kwargs to the factory."""
        self.kwargs = json.dumps(data)
        return self

    and_data = with_data

    @beat("{} creates test data using {factory_class}")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to create the test data."""
        the_actor.attempts_to(
            SendPOSTRequest.to(DATA_FACTORY_URL).with_(
                data={
                    "factory_class": self.factory_class,
                    "kwargs_json": self.kwargs,
                    "receipt_items": self.receipt_items,
                },
            ),
        )

        the_actor.should(
            See.the(StatusCodeOfTheLastResponse(), IsEqualTo(200)),
            See.the(BodyOfTheLastResponse(), ContainsTheKey("pk")),
        )

        if self.receipt_items:
            director = Director()
            last_response = BodyOfTheLastResponse().answered_by(the_actor)
            for item in self.receipt_items.split(","):
                name = self.receipt_map[item] if item in self.receipt_map else item
                director.notes(name, last_response[item])

    def __init__(self, factory_class: str) -> None:
        self.factory_class = factory_class
        self.kwargs = ""
        self.receipt_items = ""
        self.receipt_map = {}
