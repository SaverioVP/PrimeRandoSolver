from dataclasses import dataclass
from typing import Optional, Dict, Any
from enums import Items

@dataclass
class ItemPickup:
    itype: Items
    reqs: Optional[Dict[str, Any]] = None