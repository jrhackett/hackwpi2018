class BaseItem:
    """
    Provides an interface for any item
    """
    name: str
    weight: float

    def use_item(self):
        pass
