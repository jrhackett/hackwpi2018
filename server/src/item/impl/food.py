from server.src.item.base_item import BaseItem


class Food(BaseItem):
    """
    Food is a basic consumable resource that is used to satisfy hunger
    """
    def __init__(self):
        super().__init__()
        self.name = "Food"
        self.weight = 2.0
