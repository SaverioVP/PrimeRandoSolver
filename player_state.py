from enums import Items, GameEvents


class PlayerState:
    def __init__(self):
        # Initialize inventory with 0 values
        self.inventory = {item: 0 for item in Items}
        self.events = {event: 0 for event in GameEvents}

    def add_item(self, item, count=1):
        """Add an item or increase count for expansions/tanks."""
        if item in self.inventory:
            # Countable items
            if item in (Items.MISSILE_EXPANSION, Items.ENERGY_TANK):
                self.inventory[item] += count
            else:
                # Binary items (0 → 1 only)
                self.inventory[item] = 1
        else:
            raise ValueError(f"Unknown item: {item}")

    def has_item(self, item, count=1) -> bool:
        """Check if player has the item (or enough countable ones)."""
        if item not in self.inventory:
            return False
        return self.inventory[item] >= count

    def trigger_event(self, event):
        """Mark a game event as completed."""
        if event in self.events:
            self.events[event] = 1
        else:
            raise ValueError(f"Unknown event: {event}")

    def has_event(self, event) -> bool:
        """Check if the game event has been triggered."""
        return self.events.get(event, 0) == 1

    def can_satisfy(self, reqs: list) -> bool:
        """
        Check if all requirements (items/events) are satisfied.
        Reqs can contain Items, GameEvents, or (Items, count).
        """
        for req in reqs:
            if isinstance(req, tuple):
                # Countable item requirement: (Item, count)
                item, count = req
                if not self.has_item(item, count):
                    return False
            elif isinstance(req, Items):
                if not self.has_item(req):
                    return False
            elif isinstance(req, GameEvents):
                if not self.has_event(req):
                    return False
            else:
                raise ValueError(f"Unknown requirement type: {req}")
        return True
