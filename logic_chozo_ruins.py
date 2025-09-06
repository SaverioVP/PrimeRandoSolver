from enums import Items, GameEvents
from item_pickup import ItemPickup

area_logic = {
    "Transport to Tallon Overworld North": {
        "doors_to": {
            "Transport to Chozo Ruins West": None,
            "Ruins Entrance": None,
        },
    },
    "Ruins Entrance": {
        "doors_to": {
            "Transport to Tallon Overworld North": None,
            "Main Plaza": None,
        }
    },
    "Main Plaza (Floor)": {
        "pickups": [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.MORPH_BALL, Items.BOOST_BALL]}
            ),
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION,
                reqs={"ALL": [Items.SUPER_MISSILE]}
            ),
        ],
        "doors_to": {
            "Ruins Entrance": None,
            "Ruined Shrine Access": {"ALL": [Items.MISSILES]},
            "Nursery Access": None,
            "Ruined Fountain Access": None,
        }
    },
    "Main Plaza (Vault Ledge)": {
        "pickups": {
            "Energy Tank": None,
        },
        "doors_to": {
            "Main Plaza (Floor)": None,
            "Plaza Access": None,
        }
    },
    "Main Plaza (Grapple Ledge)": {
        "pickups":  [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.GRAPPLE_BEAM]}
            ),
        ],
        "doors_to": {
            "Main Plaza (Floor)": None,
            "Piston Tunnel": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Eyon Tunnel": {
        "doors_to": {
            "Nursery Acces": None,
            "Ruined Nursery": None,
        }
    },
    "Ruined Nursery": {
        "pickups":  [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.MORPH_BALL, Items.BOMBS]}
            ),
        ],
        "doors_to": {
            "Eyon Tunnel": None,
            "North Atrium": None,
            "Save Station 1": None,
        }
    },
    "Save Station 1": {
        "doors_to": {
            "Ruined Nursery": None,
        }
    },
    "North Atrium": {
        "doors_to": {
            "Ruined Nursery": None,
            "Ruined Gallery": None
        }
    },
    "Ruined Gallery": {
        "pickups":  [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.MISSILES]}
            ),
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.MORPH_BALL]}
            ),
        ],
        "doors_to": {
            "Chozo Map Station": {"ALL": [Items.MISSILES]},
            "Totem Access": None,
        }
    },
    "Chozo Map Station": {
        "doors_to": {
            "Ruined Gallery": None
        }
    },
    "Totem Access": {
        "doors_to": {
            "Ruined Gallery": None,
            "Hive Totem": None,
        }
    },
    "Hive Totem": {
        "pickups": {
            "Missiles": {"ALL": [GameEvents.HIVE_MECHA_DEFEATED]}
        },
        "doors_to": {
            "Totem Access": None,
            "Transport Access North": {"ALL": [Items.MISSILES]}
        }
    },
    "Transport Access North": {
        "pickups": {
            "Energy Tank": None
        },
        "doors_to": {
            "Hive Totem": None,
            "Transport to Magmoor Caverns North": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Transport to Magmoor Caverns North": {
        "doors_to": {
            "Transport Access North": None,
            "Vault Access": None,
            "Sun Tower": None,
        },
    },
    "Vault Access": {
        "doors_to": {
            "Vault": {"ALL": [Items.MORPH_BALL]},
            "Transport to Magmoor Caverns North": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Vault": {
        "pickups": {
            "Missile Expansion": {"ALL": [Items.MORPH_BALL, Items.BOMBS]}
        },
        "doors_to": {
            "Vault Access": None,
            "Plaza Access": None,
        }
    },
    "Plaza Access": {
        "doors_to": {
            "Main Plaza (Vault Ledge)": None,
            "Vault": None
        }
    },
    "Sun Tower": {
        "doors_to": {
            "Transport to Magmoor Caverns North": None,
            "Sun Tower Access": {"ALL": [Items.MORPH_BALL, Items.SPIDER_BALL]}
        }
    },
    "Sun Tower Access": {
        "doors_to": {
            "Sun Tower": None,
            "Sunchamber": None,
        }
    },
    "Sunchamber": {
        "pickups": {
            "Varia Suit": {"ALL": [GameEvents.FLAAHGRA_DEFEATED]},
            "Artifact_Wild": {"ALL": [GameEvents.FLAAHGRA_DEFEATED, Items.ICE_BEAM, Items.XRAY_VISOR]},  # Acquiring Ice Beam required to trigger the chozo ghost spawn
        }
    },
    "Sunchamber Access": {
        "doors_to": {
            "Sunchamber": {"NOT": [GameEvents.FLAAHGRA_DEFEATED]},
            "Sunchamber Lobby": None,
        }
    },
    "Sunchamber Lobby": {
        "doors_to": {
            "Sunchamber Access": None,
            "Arboretum": None,
        }
    },
    "Arboretum": {
        "doors_to": {
            "Sunchamber Lobby": {"ALL": [Items.MORPH_BALL, Items.MISSILES]},
            "Arboretum Access": None,
            "Gathering Hall Access": {"ALL": [Items.MISSILES]}
        }
    },
    "Arboretum Access": {
        "doors_to": {
            "Arboretum": {"ALL": [Items.MISSILES]},
            "Ruined Fountain": None,
        }
    },
    "Ruined Fountain": {
        "pickups":[
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION, 
                reqs={"ALL": [Items.MORPH_BALL, Items.SPIDER_BALL]}
            ),
        ],
        "doors_to": {
            "Arboretum_Access": None,
            "Meditation Fountain": None,
            "Ruined Fountain Access": None,
        }
    },
    "Ruined Fountain Access": {
        "doors_to": {
            "Main Plaza (Floor)": {"ALL": [Items.MORPH_BALL]},
            "Ruined Fountain": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Meditation Fountain": {
        "doors_to": {
            "Ruined Fountain": None,
            "Magma Pool": None
        }
    },
    "Magma Pool (Close Side)": {
        "doors_to": {
            "Meditation Fountain": None,
            "Magma Pool (Far Side)": {"ALL": [Items.GRAPPLE_BEAM, Items.VARIA_SUIT]},
        }
    },
    "Magma Pool (Far Side)": {
        "pickups": [
            ItemPickup(
                item_type=Items.POWER_BOMB, # this logic is covered in access requirements for magma pool crossing
                reqs=None
            ),
        ],
        "doors_to": {
            "Magma Pool (Close Side)": {"ALL": [Items.GRAPPLE_BEAM, Items.VARIA_SUIT]},
            "Training Chamber Access": {"ALL": [Items.WAVE_BEAM]},
        }
    },
    "Training Chamber Access": {
        "pickups": [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION,
                reqs=None
            ),
        ],
        "doors_to": {
            "Magma Pool": {"ALL": [Items.WAVE_BEAM]},
            "Training Chamber": {"ALL": [Items.WAVE_BEAM]},
        }
    },
    "Training Chamber": {
        "pickups": [
            ItemPickup(
                item_type=Items.ENERGY_TANK,
                reqs=None
            ),
        ],
        "doors_to": {
            "Training Chamber Access": {"ALL": [Items.WAVE_BEAM]},
            "Piston Tunnel": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Piston Tunnel": {
        "doors_to": {
            "Training Chamber": {"ALL": [Items.MORPH_BALL]},
            "Main Plaza (Grapple Ledge)": {"ALL": [Items.MORPH_BALL]}
        }
    },
    "Gathering Hall Access": {
        "doors_to": {
            "Arboretum": None,
            "Gathering Hall": None
        }
    },
    "Gathering Hall (Lower)": {
        "doors_to": {
            "Gathering Hall (Upper)": {"ANY": [Items.MORPH_BALL, Items.SPACE_BOOTS]},
            "Save Station 2": {"ALL": [Items.MISSILES]},
            "Water Hall Access": None,
        },
    },
    "Gathering Hall (Upper)": {
        "pickups": [
            ItemPickup(
                item_type=Items.MISSILE_EXPANSION,
                reqs={"ALL": [Items.SPACE_BOOTS]}
            ),
        ],
        "doors_to": {
            "Gathering Hall (Lower)": None,
            "East Atrium": None
        }
    },

    

}




    

