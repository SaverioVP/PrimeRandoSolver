from typing import Union, Iterable, Dict, Any
from requirement import Requirement
from enums import Locations

class Door:
    def __init__(self, target: Locations, reqs: Union[Requirement, Iterable, Dict[str, Any], None] = None):
        """
        A door connects this location to another.
        
        Args:
            target: The destination location (Locations enum member).
            reqs: The requirement(s) to traverse this door.
                  - None → always accessible
                  - Iterable of Items → ALL required
                  - Dict with "ANY" → alternatives
                  - Requirement object → use directly
        """
        self.target = target
        self.reqs = reqs if isinstance(reqs, Requirement) else Requirement(reqs)

    def can_traverse(self, inventory: set) -> bool:
        """Check if the door can be traversed given the current inventory."""
        return self.reqs.is_satisfied(inventory)

    def __repr__(self):
        return f"Door(to={self.target}, reqs={self.reqs})"