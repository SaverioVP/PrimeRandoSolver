from dataclasses import dataclass, field
from typing import Optional, Union, Iterable, Dict, Any
from enums import Items
from requirement import Requirement

@dataclass
class ItemPickup:
    itype: Items
    reqs: Requirement = field(default_factory=Requirement)

    def __init__(self, itype: Items, reqs: Union[Requirement, Iterable[Items], Dict[str, Any], None] = None):
        self.itype = itype
        self.reqs = reqs if isinstance(reqs, Requirement) else Requirement(reqs)

    def is_available(self, inventory: set) -> bool:
        """Check if this pickup can be collected with the current inventory."""
        return self.reqs.is_satisfied(inventory)

    def __repr__(self):
        return f"ItemPickup({self.itype}, reqs={self.reqs})"