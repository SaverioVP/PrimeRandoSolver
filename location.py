# location.py
from typing import List
from dataclasses import dataclass, field

from enums import Locations
from item_pickup import ItemPickup
from door import Door


@dataclass
class Location:
    """Represents a single room/location in the world graph."""
    name: Locations
    pickups: List[ItemPickup] = field(default_factory=list)
    doors: List[Door] = field(default_factory=list)

    def available_pickups(self, inventory: set) -> List[ItemPickup]:
        """Return all pickups in this location that can be collected with current inventory."""
        return [p for p in self.pickups if p.is_available(inventory)]

    def available_doors(self, inventory: set) -> List[Door]:
        """Return all doors from this location that can be traversed with current inventory."""
        return [d for d in self.doors if d.can_traverse(inventory)]

    def __repr__(self):
        return f"Location({self.name}, pickups={len(self.pickups)}, doors={len(self.doors)})"
