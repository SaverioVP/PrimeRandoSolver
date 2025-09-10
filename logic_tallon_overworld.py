from enums import Items, GameEvents, Locations
from item_pickup import ItemPickup
from door import Door
from location import Location

area_logic = {
    Locations.TALLON_LANDING_SITE_FLOOR: Location(
        doors=[
            Door(Locations.TALLON_WATER_FALL_CAVERN),
            Door(Locations.TALLON_TEMPLE_HALL),
            Door(Locations.TALLON_CANYON_CAVERN),
            Door(Locations.TALLON_LANDING_SITE_LEDGE, reqs=[Items.SPACE_BOOTS])
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.MORPH_BALL])
        ]
    ),
    Locations.TALLON_LANDING_SITE_LEDGE: Location(
        doors=[
            Door(Locations.TALLON_ALCOVE),
            Door(Locations.TALLON_GULLY),
            Door(Locations.TALLON_LANDING_SITE_FLOOR)
        ]
    ),
    Locations.TALLON_ALCOVE: Location(
        doors=[
            Door(Locations.TALLON_LANDING_SITE_LEDGE)
        ],
        pickups=[
            ItemPickup(Items.SPACE_BOOTS)
        ]
    ),
    Locations.TALLON_TALLON_CANYON: Location(
        doors=[
            Door(Locations.TALLON_CANYON_CAVERN),
            Door(Locations.TALLON_GULLY, reqs=[Items.MORPH_BALL, Items.BOOST_BALL]),
            Door(Locations.TALLON_TRANSPORT_TUNNEL_A),
            Door(Locations.TALLON_ROOT_TUNNEL)
        ]
    ),
    Locations.TALLON_ROOT_TUNNEL: Location(
        doors=[
            Door(Locations.TALLON_TALLON_CANYON),
            Door(Locations.TALLON_ROOT_CAVE, reqs=[Items.MISSILES])
        ]
    ),
    Locations.TALLON_ROOT_CAVE: Location(
        doors=[
            Door(Locations.TALLON_ROOT_TUNNEL),
            Door(Locations.TALLON_ARBOR_CHAMBER, reqs=[Items.GRAPPLE_BEAM, Items.PLASMA_BEAM]),
            Door(Locations.TALLON_TRANSPORT_TUNNEL_B)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.XRAY_VISOR, Items.GRAPPLE_BEAM])
        ]
    ),
    Locations.TALLON_ARBOR_CHAMBER: Location(
        doors=[
            Door(Locations.TALLON_ROOT_CAVE)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION)
        ]
    ),
    Locations.TALLON_TRANSPORT_TUNNEL_B: Location(
        doors=[
            Door(Locations.TALLON_ROOT_CAVE),
            Door(Locations.TALLON_TRANSPORT_TO_MAGMOOR_CAVERNS_EAST)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.SPACE_BOOTS])
        ]
    ),
    Locations.TALLON_TRANSPORT_TUNNEL_A: Location(
        doors=[
            Door(Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_WEST),
            Door(Locations.TALLON_TALLON_CANYON)
        ]
    ),
    Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_WEST: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_NORTH)
        ]
    ),
    Locations.TALLON_TEMPLE_HALL: Location(
        doors=[
            Door(Locations.TALLON_LANDING_SITE_FLOOR),
            Door(Locations.TALLON_TEMPLE_SECURITY_STATION)
        ]
    ),
    Locations.TALLON_TEMPLE_SECURITY_STATION: Location(
        doors=[
            Door(Locations.TALLON_TEMPLE_HALL),
            Door(Locations.TALLON_TEMPLE_LOBBY, reqs=[Items.MISSILES])
        ]
    ),
    Locations.TALLON_TEMPLE_LOBBY: Location(
        doors=[
            Door(Locations.TALLON_TEMPLE_SECURITY_STATION),
            Door(Locations.TALLON_ARTIFACT_TEMPLE)
        ]
    ),
    Locations.TALLON_ARTIFACT_TEMPLE: Location(
        doors=[
            Door(Locations.TALLON_TEMPLE_LOBBY),
            Door(Locations.TALLON_IMPACT_CRATER, reqs=[Items.BOSS_META_RIDLEY])
        ],
        pickups=[
            ItemPickup(Items.ARTIFACT_TRUTH)
        ]
    ),    
    Locations.TALLON_WATER_FALL_CAVERN: Location(
        doors=[
            Door(Locations.TALLON_LANDING_SITE_FLOOR),
            Door(Locations.TALLON_FRIGATE_CRASH_SITE, reqs=[Items.MORPH_BALL, Items.MISSILES])
        ]
    ),
    # --- Frigate Site ---
    Locations.TALLON_FRIGATE_CRASH_SITE_NEAR: Location(
        doors=[
            Door(Locations.TALLON_WATER_FALL_CAVERN),
            Door(Locations.TALLON_FRIGATE_CRASH_SITE_FAR, reqs=[Items.MORPH_BALL, Items.BOMBS]),  # or Grapple Beam
        ]
    ),
    Locations.TALLON_FRIGATE_CRASH_SITE_FAR: Location(
        doors=[
            Door(Locations.TALLON_FRIGATE_CRASH_SITE_NEAR),
            Door(Locations.TALLON_OVERGROWN_CAVERN, reqs=[Items.SPACE_BOOTS, Items.ICE_BEAM]),
            Door(Locations.TALLON_FRIGATE_ACCESS_TUNNEL, reqs=[Items.ICE_BEAM])
        ]
    ),
    Locations.TALLON_OVERGROWN_CAVERN: Location(
        doors=[
            Door(Locations.TALLON_FRIGATE_CRASH_SITE_FAR, reqs=[Items.ICE_BEAM]),
            Door(Locations.TALLON_TRANSPORT_TUNNEL_C, reqs=[Items.ICE_BEAM])
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION)
        ]
    ),
    Locations.TALLON_TRANSPORT_TUNNEL_C: Location(
        doors=[
            Door(Locations.TALLON_OVERGROWN_CAVERN, reqs=[Items.ICE_BEAM]),
            Door(Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_EAST, reqs=[Items.ICE_BEAM])
        ]
    ),
    Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_EAST: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_EAST)
        ]
    ),
    Locations.TALLON_FRIGATE_ACCESS_TUNNEL: Location(
        doors=[
            Door(Locations.TALLON_FRIGATE_CRASH_SITE_FAR),
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_C)
        ]
    ),

    # --- Frigate Interior ---
    Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_C: Location(
        doors=[
            Door(Locations.TALLON_FRIGATE_ACCESS_TUNNEL),
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_B)
        ]
    ),
    Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_B: Location(
        doors=[
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_C),
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_A)
        ]
    ),
    Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_A: Location(
        doors=[
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_B),
            Door(Locations.TALLON_REACTOR_CORE)
        ]
    ),
    Locations.TALLON_REACTOR_CORE: Location(
        doors=[
            Door(Locations.TALLON_MAIN_VENTILATION_SHAFT_SECTION_A)
        ],
        reqs=[Items.SPACE_BOOTS, Items.THERMAL_VISOR, Items.WAVE_BEAM]  # gravity suit alternative
    ),
    Locations.TALLON_REACTOR_ACCESS: Location(
        doors=[
            Door(Locations.TALLON_REACTOR_CORE, reqs=[Items.THERMAL_VISOR, Items.WAVE_BEAM]),
            Door(Locations.TALLON_SAVE_STATION)
        ]
    ),
    Locations.TALLON_SAVE_STATION: Location(
        doors=[
            Door(Locations.TALLON_REACTOR_ACCESS)
        ]
    ),
    Locations.TALLON_CARGO_FREIGHT_LIFE_TO_DECK_GAMMA: Location(
        doors=[
            Door(Locations.TALLON_REACTOR_ACCESS),
            Door(Locations.TALLON_DECK_BETA_TRANSIT_HALL)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.MISSILES])
        ]
    ),
    Locations.TALLON_DECK_BETA_TRANSIT_HALL: Location(
        doors=[
            Door(Locations.TALLON_CARGO_FREIGHT_LIFE_TO_DECK_GAMMA),
            Door(Locations.TALLON_BIOHAZARD_CONTAINMENT)
        ]
    ),
    Locations.TALLON_BIOHAZARD_CONTAINMENT: Location(
        doors=[
            Door(Locations.TALLON_DECK_BETA_TRANSIT_HALL),
            Door(Locations.TALLON_DECK_BETA_SECURITY_HALL)
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION)
        ]
    ),
    Locations.TALLON_DECK_BETA_SECURITY_HALL: Location(
        doors=[
            Door(Locations.TALLON_BIOHAZARD_CONTAINMENT),
            Door(Locations.TALLON_BIOTECH_RESEARCH_AREA_1)
        ]
    ),
    Locations.TALLON_BIOTECH_RESEARCH_AREA_1: Location(
        doors=[
            Door(Locations.TALLON_DECK_BETA_SECURITY_HALL),
            Door(Locations.TALLON_DECK_BETA_CONDUIT_HALL)
        ]
    ),
    Locations.TALLON_DECK_BETA_CONDUIT_HALL: Location(
        doors=[
            Door(Locations.TALLON_BIOTECH_RESEARCH_AREA_1),
            Door(Locations.TALLON_CONNECTION_ELEVATOR_TO_DECK_BETA)
        ]
    ),
    Locations.TALLON_CONNECTION_ELEVATOR_TO_DECK_BETA: Location(
        doors=[
            Door(Locations.TALLON_DECK_BETA_CONDUIT_HALL)
        ]
    ),
    Locations.TALLON_HYDRO_ACCESS_TUNNEL: Location(
        doors=[
            Door(Locations.TALLON_DECK_BETA_CONDUIT_HALL)
        ],
        pickups=[
            ItemPickup(Items.ENERGY_TANK)
        ]
    ),
    # --- Great Tree ---
    Locations.TALLON_GREAT_TREE_HALL_LOWER: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_UPPER),  # gate logic unknown
            Door(Locations.TALLON_TRANSPORT_TUNNEL_D, reqs=[Items.ICE_BEAM])
        ]
    ),
    Locations.TALLON_GREAT_TREE_HALL_UPPER: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_LOWER),
            Door(Locations.TALLON_GREAT_TREE_CHAMBER, reqs=[Items.XRAY_VISOR, Items.SPACE_BOOTS])
        ]
    ),
    Locations.TALLON_TRANSPORT_TUNNEL_D: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_LOWER),
            Door(Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_SOUTH)
        ]
    ),
    Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_SOUTH: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_SOUTH)
        ]
    ),
    Locations.TALLON_GREAT_TREE_CHAMBER: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_UPPER)
        ]
    ),
    Locations.TALLON_LIFE_GROVE_TUNNEL: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_UPPER),
            Door(Locations.TALLON_LIFE_GROVE, reqs=[Items.BOOST_BALL]),
        ],
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, reqs=[Items.BOOST_BALL, Items.BOMBS])
        ]
    ),
    Locations.TALLON_TRANSPORT_TUNNEL_E: Location(
        doors=[
            Door(Locations.TALLON_GREAT_TREE_HALL_LOWER),
            Door(Locations.TALLON_TRANSPORT_TO_PHAZON_MINES_EAST)
        ]
    ),
    Locations.TALLON_LIFE_GROVE: Location(
        doors=[
            Door(Locations.TALLON_LIFE_GROVE_TUNNEL)
        ],
        pickups=[
            ItemPickup(Items.XRAY_VISOR),
            ItemPickup(Items.ARTIFACT_CHOZO)
        ]
    ),
    Locations.TALLON_TRANSPORT_TO_PHAZON_MINES_EAST: Location(
        doors=[
            Door(Locations.PHAZON_TRANSPORT_TO_TALLON_OVERWORLD_SOUTH)
        ]
    ),
}