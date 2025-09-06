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