from enums import Items, GameEvents, Locations
from item_pickup import ItemPickup
from door import Door
from location import Location
from game_event import GameEvent

area_logic = {
    Locations.MAGMOOR_TRANSPORT_TO_CHOZO_RUINS_NORTH: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_MAGMOOR_CAVERNS_NORTH),
            Door(Locations.MAGMOOR_BURNING_TRAIL)
        ]
    ),
    Locations.MAGMOOR_BURNING_TRAIL: Location(
        doors=[
            Door(Locations.MAGMOOR_TRANSPORT_TO_CHOZO_RUINS_NORTH),
            Door(Locations.MAGMOOR_SAVE_STATION_MAGMOOR_A),
            Door(Locations.MAGMOOR_LAKE_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_SAVE_STATION_MAGMOOR_A: Location(
        doors=[
            Door(Locations.MAGMOOR_BURNING_TRAIL)
        ]
    ),
    Locations.MAGMOOR_LAKE_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_BURNING_TRAIL),
            Door(Locations.MAGMOOR_LAVA_LAKE)
        ]
    ),
    Locations.MAGMOOR_LAVA_LAKE: Location(
        pickups=[
            ItemPickup(Items.ARTIFACT_NATURE, [Items.MISSILES, Items.SPACE_BOOTS])
        ],
        doors=[
            Door(Locations.MAGMOOR_LAKE_TUNNEL),
            Door(Locations.MAGMOOR_PIT_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_PIT_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_LAVA_LAKE),
            Door(Locations.MAGMOOR_TRICLOPS_PIT)
        ]
    ),
    Locations.MAGMOOR_TRICLOPS_PIT: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.XRAY_VISOR, Items.SPACE_BOOTS, Items.MISSILES]),
        ],
        doors=[
            Door(Locations.MAGMOOR_PIT_TUNNEL),
            Door(Locations.MAGMOOR_STORAGE_CAVERN),
            Door(Locations.MAGMOOR_MONITOR_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_STORAGE_CAVERN: Location(
        doors=[
            Door(Locations.MAGMOOR_TRICLOPS_PIT)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION)
        ]
    ),
    Locations.MAGMOOR_MONITOR_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_TRICLOPS_PIT),
            Door(Locations.MAGMOOR_MONITOR_STATION_LOWER)
        ]
    ),
    Locations.MAGMOOR_MONITOR_STATION_LOWER: Location(
        doors=[
            Door(Locations.MAGMOOR_MONITOR_TUNNEL),
            Door(Locations.MAGMOOR_SHORE_TUNNEL),
            Door(Locations.MAGMOOR_MONITOR_STATION_UPPER),
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_A)
        ]
    ),
    Locations.MAGMOOR_MONITOR_STATION_UPPER: Location(
        doors=[
            Door(Locations.MAGMOOR_MONITOR_STATION_LOWER),
            Door(Locations.MAGMOOR_MONITOR_STATION_UPPER_LEDGE, reqs=[GameEvents.MONITOR_STATION_MOVED, Items.SPACE_BOOTS])
        ],
        events=[
            GameEvent(GameEvents.MONITOR_STATION_MOVED, reqs=[Items.BOOST_BALL])
        ]
    ),
    Locations.MAGMOOR_MONITOR_STATION_UPPER_LEDGE: Location(
        doors=[
            Door(Locations.MAGMOOR_WARRIOR_SHRINE),
            Door(Locations.MAGMOOR_MONITOR_STATION_UPPER)
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TUNNEL_A: Location(
        doors=[
            Door(Locations.MAGMOOR_MONITOR_STATION_LOWER),
            Door(Locations.MAGMOOR_TRANSPORT_TO_PHENDRANA_DRIFTS_NORTH)
        ],
        pickups=[
            ItemPickup(Items.ENERGY_TANK, [Items.BOMBS])
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TO_PHENDRANA_DRIFTS_NORTH: Location(
        doors=[
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_A),
            Door(Locations.PHENDRANA_TRANSPORT_TO_MAGMOOR_CAVERNS_WEST)
        ]
    ),
    Locations.MAGMOOR_WARRIOR_SHRINE: Location(
        doors=[
            Door(Locations.MAGMOOR_MONITOR_STATION_UPPER_LEDGE),
            Door(Locations.MAGMOOR_SHORE_TUNNEL, [Items.MORPH_BALL, Items.POWER_BOMB])
        ],
        pickups=[
            ItemPickup(Items.ARTIFACT_STRENGTH, [Items.MORPH_BALL]),
            ItemPickup(Items.POWER_BOMB, [Items.POWER_BOMB])
        ]
    ),
    Locations.MAGMOOR_SHORE_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_MONITOR_STATION_LOWER),
            Door(Locations.MAGMOOR_FIERY_SHORES),
            Door(Locations.MAGMOOR_WARRIOR_SHRINE)
        ],
        pickups=[
            ItemPickup(Items.ICE_SPREADER, [Items.POWER_BOMB])
        ]
    ),
    Locations.MAGMOOR_FIERY_SHORES: Location(
        doors=[
            Door(Locations.MAGMOOR_SHORE_TUNNEL),
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_B)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL])
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TUNNEL_B: Location(
        doors=[
            Door(Locations.MAGMOOR_FIERY_SHORES),
            Door(Locations.MAGMOOR_TRANSPORT_TO_TALLON_OVERWORLD_WEST)
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TO_TALLON_OVERWORLD_WEST: Location(
        doors=[
            Door(Locations.TALLON_TRANSPORT_TO_MAGMOOR_CAVERNS_EAST),
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_B),
            Door(Locations.MAGMOOR_TWIN_FIRES_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_TWIN_FIRES_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_TRANSPORT_TO_TALLON_OVERWORLD_WEST),
            Door(Locations.MAGMOOR_TWIN_FIRES)
        ]
    ),
    Locations.MAGMOOR_TWIN_FIRES: Location(
        doors=[
            Door(Locations.MAGMOOR_TWIN_FIRES_TUNNEL),
            Door(Locations.MAGMOOR_NORTH_CORE_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_NORTH_CORE_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_TWIN_FIRES, [Items.WAVE_BEAM]),
            Door(Locations.MAGMOOR_GEOTHERMAL_CORE, [Items.WAVE_BEAM])
        ]
    ),
    Locations.MAGMOOR_GEOTHERMAL_CORE: Location(
        doors=[
            Door(Locations.MAGMOOR_NORTH_CORE_TUNNEL),
            Door(Locations.MAGMOOR_PLASMA_PROCESSING, [Items.ICE_BEAM, Items.BOOST_BALL, Items.SPIDER_BALL]),
            Door(Locations.MAGMOOR_SOUTH_CORE_TUNNEL)
        ]
    ),
    Locations.MAGMOOR_PLASMA_PROCESSING: Location(
        doors=[
            Door(Locations.MAGMOOR_GEOTHERMAL_CORE, [Items.PLASMA_BEAM])
        ],
        pickups=[
            ItemPickup(Items.PLASMA_BEAM)
        ]
    ),
    Locations.MAGMOOR_SOUTH_CORE_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_GEOTHERMAL_CORE, [Items.WAVE_BEAM]),
            Door(Locations.MAGMOOR_MAGMOOR_WORKSTATION, [Items.WAVE_BEAM])
        ]
    ),
    Locations.MAGMOOR_MAGMOOR_WORKSTATION: Location(
        doors=[
            Door(Locations.MAGMOOR_SOUTH_CORE_TUNNEL),
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_C, [Items.WAVE_BEAM]),
            Door(Locations.MAGMOOR_WORKSTATION_TUNNEL)
        ],
        pickups=[
            ItemPickup(Items.ENERGY_TANK)  # requirements???
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TUNNEL_C: Location(
        doors=[
            Door(Locations.MAGMOOR_MAGMOOR_WORKSTATION, [Items.WAVE_BEAM]),
            Door(Locations.MAGMOOR_TRANSPORT_TO_PHENDRANA_DRIFTS_SOUTH, [Items.WAVE_BEAM])
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TO_PHENDRANA_DRIFTS_SOUTH: Location(
        doors=[
            Door(Locations.MAGMOOR_TRANSPORT_TUNNEL_C, [Items.WAVE_BEAM]),
            Door(Locations.PHENDRANA_TRANSPORT_TO_MAGMOOR_CAVERNS_SOUTH),
            Door(Locations.MAGMOOR_SAVE_STATION_MAGMOOR_B)
        ]
    ),
    Locations.MAGMOOR_SAVE_STATION_MAGMOOR_B: Location(
        doors=[Door(Locations.MAGMOOR_TRANSPORT_TO_PHENDRANA_DRIFTS_SOUTH)]
    ),
    Locations.MAGMOOR_WORKSTATION_TUNNEL: Location(
        doors=[
            Door(Locations.MAGMOOR_MAGMOOR_WORKSTATION),
            Door(Locations.MAGMOOR_TRANSPORT_TO_PHAZON_MINES_WEST, [Items.ICE_BEAM])
        ]
    ),
    Locations.MAGMOOR_TRANSPORT_TO_PHAZON_MINES_WEST: Location(
        doors=[
            Door(Locations.MAGMOOR_WORKSTATION_TUNNEL, [Items.ICE_BEAM])
            ]
    )
}