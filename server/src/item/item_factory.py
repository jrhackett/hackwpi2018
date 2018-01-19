from server.src.item.items import ItemType
from server.src.item.base_item import BaseItem
from server.src.item import impl


class ItemFactory:
    """
    Handles the creation of any new items
    """

    @staticmethod
    def make_item(item_type: ItemType) -> BaseItem:
        if item_type == ItemType.FOOD:
            item = impl.Food()
        elif item_type == ItemType.WATER:
            item = impl.Water()
        else:
            raise NotImplementedError('Provided item type {} has not been implemented!'.format(item_type))

        return item
