from server.src.item.base_item import BaseItem


class Water(BaseItem):
    """
    Water is a basic consumable resource that is used to satisfy thirst
    """
    def __init__(self):
        super().__init__()
        self.name = "Water"
        self.weight = 1.0
