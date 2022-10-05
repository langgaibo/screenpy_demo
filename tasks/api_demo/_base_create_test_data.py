"""
Task to create a helper class for test data using the Data Factory endpoint.
"""

import json
from typing import Any, Dict, List, Union


class _BaseCreateTestData:
    """Create a helper for test data using the backend factories.

    Examples::

        # this class is not meant to be used directly, here are some examples using
        # its children

        the_actor.attempts_to(
            CreateTestData.using("customers.tests.factories.CustomerCartFactory"),
        )

        the_actor.attempts_to(
            CreateTestData.using("customers.tests.factories.CustomerCartFactory")
            .with_data(
                {"customer_id": CUSTOMER_PK, "item__pk": ITEM_PK}
            ).and_receipt("discount_applied", {"item.discount": "coupon"}),
        )

        # in a derived class:
        the_actor.attempts_to(
            CreateTestCustomer().with_overrides(
                user__email="coolcustomer@example.com"
            ).named("Cool Customer"),
        )
    """

    updates = {}
    name = "REPLACE ME, children classes should set default name"
    kwargs = {}
    receipt_map = {}
    receipt_items = ""

    def with_data(self, data: dict) -> "_BaseCreateTestData":
        """Set the data to pass as kwargs to the factory."""
        self.kwargs = json.dumps(data)
        return self

    and_data = with_data

    def with_receipt(self, *items: Union[Dict[str, str], str]) -> "_BaseCreateTestData":
        """Set the extra receipt items to request back.

        These items will be noted by the Director. You can retrieve them later
        by using screenpy.directions.the_noted, using the same name as was
        passed in to this method. You can also provide more descriptive names
        by passing in a dictionary. You can mix-and-match if you'd like.

        Examples::

            .with_receipt("user.pk")
            .with_receipt({"user.pk": "test user ID"})
            .with_receipt("user.pk", {"user.email": "test user email"})
        """
        properties: List[str] = []
        named_items: Dict[str, str] = {}
        for item in items:
            try:
                # see if the item is a dict
                properties += list(item.keys())  # type: ignore
                named_items |= item  # type: ignore
            except AttributeError:
                # must not have been!
                properties.append(item)  # type: ignore
        self.receipt_items = ",".join(properties)
        self.receipt_map = named_items
        return self

    and_receipt = with_receipt

    def with_overrides(self, **kwargs: Any) -> "_BaseCreateTestData":
        """Supply optional values to be added or modified."""
        self.updates |= kwargs
        return self

    def named(self, name: str) -> "_BaseCreateTestData":
        """Supply optional receipt name."""
        self.name = name
        return self
