import pytest
from server.src.item.items import ItemType
from server.src.item.item_factory import ItemFactory
from server.src.item.base_item import BaseItem


class TestItems:

    @pytest.mark.parametrize('item_type, expected_name, expected_weight', [
        (ItemType.FOOD, 'Food', 2.0),
        (ItemType.WATER, 'Water', 1.0),
    ])
    def test_agent_symbols_and_enumerations(self, item_type: ItemType, expected_name: str, expected_weight: float):
        item: BaseItem = ItemFactory.make_item(item_type)
        assert item.name == expected_name
        assert item.weight == expected_weight

