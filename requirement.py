from typing import Iterable, Union, Tuple
from enums import Items, GameEvents

class Requirement:
    def __init__(self, items: Union[Iterable, dict, None] = None):
        if items is None:
            self.items = []
            self.any_groups = None
            self.not_items = []
        elif isinstance(items, dict):
            self.items = []
            self.any_groups = [Requirement(sub) for sub in items.get("ANY", [])] if "ANY" in items else None
            self.not_items = items.get("NOT", [])
        else:
            self.items = list(items)
            self.any_groups = None
            self.not_items = []

    def is_satisfied(self, inventory) -> bool:
        """
        inventory must be an Inventory object.
        Supports:
        - Items.MORPH_BALL (simple membership)
        - (Items.MISSILE_EXPANSION, 5) (requires at least 5)
        """
        if self.any_groups is not None:
            return any(sub.is_satisfied(inventory) for sub in self.any_groups)

        # ALL + NOT
        all_ok = all(self._has(inventory, x) for x in self.items)
        not_ok = all(not self._has(inventory, x) for x in self.not_items)
        return all_ok and not_ok

    def _has(self, inventory, requirement) -> bool:
        # Handle quantity tuples
        if isinstance(requirement, tuple):
            item, count = requirement
            return inventory.count(item) >= count
        # Handle normal items or events
        return requirement in inventory

    def __repr__(self):
        return f"Requirement(ALL={self.items}, ANY={self.any_groups}, NOT={self.not_items})"
