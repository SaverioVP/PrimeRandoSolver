area_logic = {
    "Landing Site (Floor)": {
        "pickups": {
            "Missile Expansion": {"ALL": ["Morph Ball"]}
        },
        "doors_to": {
            "Waterfall Canyon": None,
            "Temple Hall": None,
            "Canyon Cavern": None,
            "Landing Site (Ledge)": {"ALL": ["Space Jump Boots"]}
        },
    },
    "Landing Site (Ledge)":{
        "doors_to": {
            "Alcove": None,
            "Gully": None,
            "Landing Site (Floor)": None
        }
    },
    "Alcove": {
        "pickups": {
            "Space Jump Boots": None
        },
        "doors_to": {
            "Landing Site (Ledge)": None
        }
    },
    "Canyon Cavern":{
        "doors_to": {
            "Landing Site Floor": None, 
            "Tallon Canyon": None
        }
    },
    "Tallon Canyon": {
        "doors_to": {
            "Canyon Cavern": None,
            "Gully": {"ALL": ["Morph Ball", "Boost Ball"]},
            "Transport Tunnel A": None,
            "Root Tunnel": None
        }
    },
    "Root Tunnel": {
        "doors_to": {
            "Tallon Canyon": None,
            "Root Cave": {"ALL": ["Missiles"]},
        }
    },
    "Root Cave":{
        "pickups": {
            "Missile Expansion": {"ALL": ["X-Ray Visor", "Grapple Beam"]}
        },
        "doors_to": {
            "Root Tunnel": None,
            "Arbor Chamber": {"ALL": ["Grapple Beam", "Plasma Beam"]},
            "Transport Tunnel B": None
            }
    },
    "Arbor Chamber":{
        "pickups": {
            "Missile Expansion": None
        },
        "doors_to": {
            "Root Cave": None
        }
    },
    "Transport Tunnel B": {
        "pickups": {
            "Missile Expansion": {"ALL": ["Space Jump Boots"]}
        },
        "doors_to": {
            "Root Cave": None,
            "Transport to Magmoor Caverns East": None
        }
    },
    "Transport Tunnel A": {
        "doors_to": {
            "Transport to Chozo Ruins West": None,
            "Tallon Canyon": None
        }
    },
    "Transport to Chozo Ruins West": {
        "doors_to": {
            "Transport to Tallon Overworld North": None,
        }
    },
    "Temple Hall": {
        "doors_to": {
            "Landing Site": None,
            "Temple Security Station": None
        }
    },
    "Temple Security Station": {
        "doors_to": {
            "Temple Hall": None,
            "Temple Lobby": {"ALL": ["Missiles"]},
        }
    },
    "Temple Lobby": {
        "doors_to": {
            "Temple Security Station": None,
            "Artifact Temple": None
        }
    },
    "Artifact Temple": {
        "pickups": {
            "Artifact_Truth": None,
        },
        "doors_to": {
            "Temple Lobby": None,
            "Impact Crater": {"ALL": ["BOSS_MetaRidley"]}
        }
    },
    "Waterfall Cavern": {
        "doors_to": {
            "Landing Site": None,
            "Frigate Crash Site": {"ALL": ["Morph Ball", "Missiles"]}
        }
    }

}

    # --- Tallon Overworld ---
    # Landing Site / West
    TALLON_LANDING_SITE = auto()
    TALLON_CANYON_CAVERN = auto()
    TALLON_TALLON_CANYON = auto()
    TALLON_GULLY = auto()
    TALLON_ALCOVE = auto()
    TALLON_ROOT_TUNNEL = auto()
    TALLON_ROOT_CAVE = auto()
    TALLON_ARBOR_CHAMBER = auto()
    TALLON_TRANSPORT_TUNNEL_B = auto()
    TALLON_TRANSPORT_TO_MAGMOOR_CAVERNS_EAST = auto()
    TALLON_TRANSPORT_TUNNEL_A = auto()
    TALLON_TRANSPORT_TO_CHOZO_RUINS_WEST = auto()
    # Artifact temple
    TALLON_TEMPLE_HALL = auto()
    TALLON_TEMPLE_SECURITY_STATION = auto()
    TALLON_TEMPLE_LOBBY = auto()
    TALLON_ARTIFACT_TEMPLE = auto()
    # Frigate site
    TALLON_WATER_FALL_CAVERN = auto()
    TALLON_FRIGATE_CRASH_SITE = auto()
    TALLON_OVERGROWN_CAVERN = auto()
    TALLON_TRANSPORT_TUNNEL_C = auto()
    TALLON_TRANSPORT_TO_CHOZO_RUINS_EAST = auto()
    TALLON_FRIGATE_ACCESS_TUNNEL = auto()
    # Frigate
    TALLON_MAIN_VENTILATION_SHAFT_SECTION_C = auto()
    # Going from B to A requires wave beam (thermal visor optional to see the conduit)
    # logic A to B unknown
    TALLON_MAIN_VENTILATION_SHAFT_SECTION_B = auto()
    TALLON_MAIN_VENTILATION_SHAFT_SECTION_A = auto()
    # Requires space jump to get around, thermal visor to see conduits and wave beam to activate the conduits
    TALLON_REACTOR_CORE = auto()
    #thermal visor + wave beam to get through access
    TALLON_REACTOR_ACCESS = auto()
    TALLON_SAVE_STATION = auto()
    # missile to break the wall for pickup
    # Cant get past from reactor onwards without gravity suit??
    TALLON_CARGO_FREIGHT_LIFE_TO_DECK_GAMMA = auto()
    TALLON_DECK_BETA_TRANSIT_HALL = auto()
    TALLON_BIOHAZARD_CONTAINMENT = auto()
    TALLON_DECK_BETA_SECURITY_HALL = auto()
    TALLON_BIOTECH_RESEARCH_AREA_1 = auto()
    TALLON_DECK_BETA_CONDUIT_HALL = auto()
    TALLON_CONNECTION_ELEVATOR_TO_DECK_BETA = auto()
    TALLON_HYDRO_ACCESS_TUNNEL = auto()
    # Great Tree
    TALLON_GREAT_TREE_HALL = auto()
    TALLON_TRANSPORT_TUNNEL_D = auto()
    TALLON_TRANSPORT_TO_CHOZO_RUINS_SOUTH = auto()
    TALLON_GREAT_TREE_CHAMBER = auto()
    TALLON_LIFE_GROVE_TUNNEL = auto()
    TALLON_TRANSPORT_TUNNEL_E = auto()
    TALLON_LIFE_GROVE = auto()
    TALLON_TRANSPORT_TO_PHAZON_MINES_EAST = auto()