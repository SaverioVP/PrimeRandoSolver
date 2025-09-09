from enums import Items, GameEvents, Locations
from item_pickup import ItemPickup
from door import Door
from location import Location

area_logic = {
    # Nursery/Vault Loop
    Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_NORTH: Location(
        doors=[
            Door(Locations.TALLON_TRANSPORT_TO_CHOZO_RUINS_WEST),
            Door(Locations.CHOZO_RUINS_ENTRANCE),
        ]
    ),
    Locations.CHOZO_RUINS_ENTRANCE: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_NORTH),
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR)
        ]
    ),
    Locations.CHOZO_MAIN_PLAZA_FLOOR: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOOST_BALL]),
            ItemPickup(Items.MISSILE_EXPANSION, [Items.SUPER_MISSILE])
        ],
        doors=[
            Door(Locations.CHOZO_RUINS_ENTRANCE),
            Door(Locations.CHOZO_RUINED_SHRINE_ACCESS, [Items.MISSILES]),
            Door(Locations.CHOZO_NURSERY_ACCESS),
            Door(Locations.CHOZO_RUINED_FOUNTAIN_ACCESS),
        ]
    ),
    Locations.CHOZO_MAIN_PLAZA_VAULT_LEDGE: Location(
        pickups=[ItemPickup(Items.ENERGY_TANK)],
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR),
            Door(Locations.CHOZO_PLAZA_ACCESS),
        ]
    ),
    Locations.CHOZO_MAIN_PLAZA_GRAPPLE_LEDGE: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.GRAPPLE_BEAM])],
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR),
            Door(Locations.CHOZO_PISTON_TUNNEL, [Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_NURSERY_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR),
            Door(Locations.CHOZO_EYON_TUNNEL),
        ]
    ),
    Locations.CHOZO_EYON_TUNNEL: Location(
        doors=[
            Door(Locations.CHOZO_NURSERY_ACCESS),
            Door(Locations.CHOZO_RUINED_NURSERY),
        ]
    ),
    Locations.CHOZO_RUINED_NURSERY: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOMBS])],
        doors=[
            Door(Locations.CHOZO_EYON_TUNNEL),
            Door(Locations.CHOZO_NORTH_ATRIUM),
            Door(Locations.CHOZO_SAVE_STATION_1),
        ]
    ),
    Locations.CHOZO_SAVE_STATION_1: Location(
        doors=[Door(Locations.CHOZO_RUINED_NURSERY)]
    ),
    Locations.CHOZO_NORTH_ATRIUM: Location(
        doors=[
            Door(Locations.CHOZO_RUINED_NURSERY),
            Door(Locations.CHOZO_RUINED_GALLERY),
        ]
    ),
    Locations.CHOZO_RUINED_GALLERY: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MISSILES]),
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL]),
        ],
        doors=[
            Door(Locations.CHOZO_CHOZO_MAP_STATION, [Items.MISSILES]),
            Door(Locations.CHOZO_TOTEM_ACCESS),
        ]
    ),
    Locations.CHOZO_CHOZO_MAP_STATION: Location(
        doors=[Door(Locations.CHOZO_RUINED_GALLERY)]
    ),
    Locations.CHOZO_TOTEM_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_RUINED_GALLERY),
            Door(Locations.CHOZO_HIVE_TOTEM),
        ]
    ),
    Locations.CHOZO_HIVE_TOTEM: Location(
        pickups=[ItemPickup(Items.MISSILES, [GameEvents.HIVE_MECHA_DEFEATED])],
        doors=[
            Door(Locations.CHOZO_TOTEM_ACCESS),
            Door(Locations.CHOZO_TRANSPORT_ACCESS_NORTH, [Items.MISSILES]),
        ]
    ),
    Locations.CHOZO_TRANSPORT_ACCESS_NORTH: Location(
        pickups=[ItemPickup(Items.ENERGY_TANK)],
        doors=[
            Door(Locations.CHOZO_HIVE_TOTEM),
            Door(Locations.CHOZO_TRANSPORT_TO_MAGMOOR_CAVERNS_NORTH, [Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_TRANSPORT_TO_MAGMOOR_CAVERNS_NORTH: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_ACCESS_NORTH),
            Door(Locations.CHOZO_VAULT_ACCESS),
            Door(Locations.CHOZO_SUN_TOWER),
        ]
    ),
    Locations.CHOZO_VAULT_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_VAULT, [Items.MORPH_BALL]),
            Door(Locations.CHOZO_TRANSPORT_TO_MAGMOOR_CAVERNS_NORTH, [Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_VAULT: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOMBS])],
        doors=[
            Door(Locations.CHOZO_VAULT_ACCESS),
            Door(Locations.CHOZO_PLAZA_ACCESS),
        ]
    ),
    Locations.CHOZO_PLAZA_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_VAULT_LEDGE),
            Door(Locations.CHOZO_VAULT),
        ]
    ),
    # Ruined Shrine/Tower of Light 
    Locations.CHOZO_RUINED_SHRINE_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR),
            Door(Locations.CHOZO_RUINED_SHRINE)
        ]
    ),
    Locations.CHOZO_RUINED_SHRINE: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOMBS]),
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOOST_BALL])
        ],
        doors=[
            # Can either jump over or roll through to get back to main plaza
            Door(Locations.CHOZO_RUINED_SHRINE_ACCESS, {"ANY": [Items.SPACE_BOOTS, Items.MORPH_BALL]}),
            Door(Locations.CHOZO_TOWER_OF_LIGHT_ACCESS, [Items.MORPH_BALL, Items.BOOST_BALL, Items.SPIDER_BALL, Items.WAVE_BEAM])
        ]
    ),
    Locations.CHOZO_TOWER_OF_LIGHT_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_RUINED_SHRINE),
            Door(Locations.CHOZO_TOWER_OF_LIGHT, [Items.WAVE_BEAM])
        ]
    ),
    Locations.CHOZO_TOWER_OF_LIGHT: Location(
        pickups=[
            ItemPickup(Items.WAVEBUSTER, reqs=[Items.MISSILES,Items.SPACE_BOOTS])
        ],
        doors=[
            Door(Locations.CHOZO_TOWER_OF_LIGHT_ACCESS, reqs=[Items.WAVE_BEAM]),
            Door(Locations.CHOZO_TOWER_CHAMBER)
        ]
    ),
    Locations.CHOZO_TOWER_CHAMBER: Location(
        pickups=[
            ItemPickup(Items.ARTIFACT_LIFEGIVER, reqs=[Items.GRAVITY_SUIT])
        ],
        doors=[
            Door(Locations.CHOZO_TOWER_OF_LIGHT)
        ]
    ),
    # Ruined Fountain / Training Chamber Loop
    Locations.CHOZO_RUINED_FOUNTAIN_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_MAIN_PLAZA_FLOOR, [Items.MORPH_BALL]),
            Door(Locations.CHOZO_RUINED_FOUNTAIN, [Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_RUINED_FOUNTAIN: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.SPIDER_BALL])],
        doors=[
            Door(Locations.CHOZO_ARBORETUM_ACCESS),
            Door(Locations.CHOZO_MEDITATION_FOUNTAIN),
            Door(Locations.CHOZO_RUINED_FOUNTAIN_ACCESS),
        ]
    ),
    Locations.CHOZO_MEDITATION_FOUNTAIN: Location(
        doors=[
            Door(Locations.CHOZO_RUINED_FOUNTAIN),
            Door(Locations.CHOZO_MAGMA_POOL_CLOSE_SIDE),
        ]
    ),
    Locations.CHOZO_MAGMA_POOL_CLOSE_SIDE: Location(
        doors=[
            Door(Locations.CHOZO_MEDITATION_FOUNTAIN),
            Door(Locations.CHOZO_MAGMA_POOL_FAR_SIDE, [Items.GRAPPLE_BEAM, Items.VARIA_SUIT]),
        ]
    ),
    Locations.CHOZO_MAGMA_POOL_FAR_SIDE: Location(
        pickups=[ItemPickup(Items.POWER_BOMB)],  # access logic covered by crossing requirements
        doors=[
            Door(Locations.CHOZO_MAGMA_POOL_CLOSE_SIDE, [Items.GRAPPLE_BEAM, Items.VARIA_SUIT]),
            Door(Locations.CHOZO_TRAINING_CHAMBER_ACCESS, [Items.WAVE_BEAM]),
        ]
    ),
    Locations.CHOZO_TRAINING_CHAMBER_ACCESS: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION)],
        doors=[
            Door(Locations.CHOZO_MAGMA_POOL_CLOSE_SIDE, [Items.WAVE_BEAM]),
            Door(Locations.CHOZO_TRAINING_CHAMBER, [Items.WAVE_BEAM]),
        ]
    ),
    Locations.CHOZO_TRAINING_CHAMBER: Location(
        pickups=[ItemPickup(Items.ENERGY_TANK)],
        doors=[
            Door(Locations.CHOZO_TRAINING_CHAMBER_ACCESS, [Items.WAVE_BEAM]),
            Door(Locations.CHOZO_PISTON_TUNNEL, [Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_PISTON_TUNNEL: Location(
        doors=[
            Door(Locations.CHOZO_TRAINING_CHAMBER, [Items.MORPH_BALL]),
            Door(Locations.CHOZO_MAIN_PLAZA_GRAPPLE_LEDGE, [Items.MORPH_BALL]),
        ]
    ),
    # Sunchamber / Sun Tower
    Locations.CHOZO_ARBORETUM_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_ARBORETUM, [Items.MISSILES]),
            Door(Locations.CHOZO_RUINED_FOUNTAIN),
        ]
    ),
    Locations.CHOZO_ARBORETUM: Location(
        doors=[
            Door(Locations.CHOZO_SUNCHAMBER_LOBBY, [Items.MORPH_BALL, Items.MISSILES]),
            Door(Locations.CHOZO_ARBORETUM_ACCESS),
            Door(Locations.CHOZO_GATHERING_HALL_ACCESS, [Items.MISSILES]),
        ]
    ),
    Locations.CHOZO_SUNCHAMBER_LOBBY: Location(
        doors=[
            Door(Locations.CHOZO_SUNCHAMBER_ACCESS),
            Door(Locations.CHOZO_ARBORETUM),
        ]
    ),
    Locations.CHOZO_SUNCHAMBER_ACCESS: Location(
        doors=[
            # Door to Sunchamber closed by invincible roots after Flaahgra defeated. Must go through Sun Tower
            Door(Locations.CHOZO_SUNCHAMBER, {"NOT": [GameEvents.FLAAHGRA_DEFEATED]}),
            Door(Locations.CHOZO_SUNCHAMBER_LOBBY),
        ]
    ),
    Locations.CHOZO_SUNCHAMBER: Location(
        pickups=[
            ItemPickup(Items.VARIA_SUIT, [GameEvents.FLAAHGRA_DEFEATED]),
            # Ice Beam required to trigger ghosts; also requires X-Ray Visor to collect Artifact
            ItemPickup(Items.ARTIFACT_WILD, [GameEvents.FLAAHGRA_DEFEATED, Items.ICE_BEAM, Items.XRAY_VISOR]),
        ]
    ),
    Locations.CHOZO_SUN_TOWER: Location(
        doors=[
            Door(Locations.CHOZO_TRANSPORT_TO_MAGMOOR_CAVERNS_NORTH),
            # Spiderball track and super missile to unlock the blocking thing
            Door(Locations.CHOZO_SUN_TOWER_ACCESS, [Items.MORPH_BALL, Items.SPIDER_BALL, Items.SUPER_MISSILE]), 
        ]
    ),
    Locations.CHOZO_SUN_TOWER_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_SUN_TOWER),
            Door(Locations.CHOZO_SUNCHAMBER),
        ]
    ),
    # Watery Hall / Dynamo
    Locations.CHOZO_GATHERING_HALL_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_ARBORETUM),
            Door(Locations.CHOZO_GATHERING_HALL_LOWER),  # treat "Gathering Hall" as the lower level
        ]
    ),
    Locations.CHOZO_GATHERING_HALL_LOWER: Location(
        doors=[
            Door(Locations.CHOZO_GATHERING_HALL_UPPER, {"ANY": [[Items.MORPH_BALL], [Items.SPACE_BOOTS]]}),
            Door(Locations.CHOZO_SAVE_STATION_2, [Items.MISSILES]),
            Door(Locations.CHOZO_WATERY_HALL_ACCESS),
        ]
    ),
    Locations.CHOZO_GATHERING_HALL_UPPER: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.SPACE_BOOTS])],
        doors=[
            Door(Locations.CHOZO_GATHERING_HALL_LOWER),
            Door(Locations.CHOZO_EAST_ATRIUM),
        ]
    ),
    Locations.CHOZO_SAVE_STATION_2: Location(
        doors=[Door(Locations.CHOZO_GATHERING_HALL_LOWER)]
    ),
    Locations.CHOZO_WATERY_HALL_ACCESS: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.MISSILES])],
        doors=[
            Door(Locations.CHOZO_GATHERING_HALL_LOWER),
            Door(Locations.CHOZO_WATERY_HALL, [Items.MISSILES]),
        ]
    ),
    Locations.CHOZO_WATERY_HALL: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.GRAVITY_SUIT]),
            ItemPickup(Items.CHARGE_BEAM, [Items.MORPH_BALL]),
        ],
        doors=[
            Door(Locations.CHOZO_WATERY_HALL_ACCESS),
            Door(Locations.CHOZO_DYNAMO_ACCESS, [Items.MISSILES, Items.MORPH_BALL]),
        ]
    ),
    Locations.CHOZO_DYNAMO_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_DYNAMO),
            Door(Locations.CHOZO_WATERY_HALL),
        ]
    ),
    Locations.CHOZO_DYNAMO: Location(
        pickups=[
            ItemPickup(Items.MISSILE_EXPANSION, [Items.MISSILES]),
            ItemPickup(Items.MISSILE_EXPANSION, [Items.SPIDER_BALL]),
        ],
        doors=[Door(Locations.CHOZO_DYNAMO_ACCESS)]
    ),
    # Energy Core / Burn Dome
    Locations.CHOZO_EAST_ATRIUM: Location(
        doors=[
            Door(Locations.CHOZO_GATHERING_HALL_UPPER),
            Door(Locations.CHOZO_ENERGY_CORE_ACCESS),
        ]
    ),
    Locations.CHOZO_ENERGY_CORE_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_EAST_ATRIUM),
            Door(Locations.CHOZO_ENERGY_CORE),
        ]
    ),
    Locations.CHOZO_ENERGY_CORE: Location(
        doors=[
            Door(Locations.CHOZO_ENERGY_CORE_ACCESS),
            Door(Locations.CHOZO_WEST_FURNACE_ACCESS, {"ANY": [[Items.MORPH_BALL, Items.BOMBS], [Items.SPACE_BOOTS]]}),
            Door(Locations.CHOZO_BURN_DOME_ACCESS),
        ]
    ),
    Locations.CHOZO_BURN_DOME_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_BURN_DOME, [Items.MORPH_BALL]),
            Door(Locations.CHOZO_ENERGY_CORE),
        ]
    ),
    Locations.CHOZO_BURN_DOME: Location(
        pickups=[
            ItemPickup(Items.BOMBS, [GameEvents.INCINERATOR_DRONE_DEFEATED]),
            ItemPickup(Items.MISSILE_EXPANSION, [GameEvents.INCINERATOR_DRONE_DEFEATED, Items.MORPH_BALL, Items.BOMBS]),
        ],
        # To leave you need bombs and to defeat the boss
        doors=[
            Door(Locations.CHOZO_BURN_DOME_ACCESS, [GameEvents.INCINERATOR_DRONE_DEFEATED, Items.MORPH_BALL, Items.BOMBS]),
        ]
    ),
    # --- Furnace / Hall of the Elders loop ---
    Locations.CHOZO_WEST_FURNACE_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_ENERGY_CORE),
            Door(Locations.CHOZO_FURNACE_ENTRANCE),
        ]
    ),
    Locations.CHOZO_FURNACE_ENTRANCE: Location(
        pickups=[ItemPickup(Items.ENERGY_TANK, [Items.MORPH_BALL, Items.BOMBS])],
        doors=[
            Door(Locations.CHOZO_FURNACE_MAIN, [Items.MORPH_BALL, Items.SPIDER_BALL, Items.BOMBS]),
            Door(Locations.CHOZO_WEST_FURNACE_ACCESS),
        ]
    ),
    Locations.CHOZO_FURNACE_MAIN: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.POWER_BOMB, Items.MORPH_BALL, Items.BOOST_BALL, Items.SPIDER_BALL])],
        doors=[
            Door(Locations.CHOZO_FURNACE_ENTRANCE, [Items.MORPH_BALL, Items.BOMBS]),
            Door(Locations.CHOZO_CROSSWAY_ACCESS_WEST, [Items.MORPH_BALL]),
            Door(Locations.CHOZO_EAST_FURNACE_ACCESS, [Items.ICE_BEAM]),
        ]
    ),
    Locations.CHOZO_CROSSWAY_ACCESS_WEST: Location(
        doors=[
            Door(Locations.CHOZO_FURNACE_MAIN),
            Door(Locations.CHOZO_CROSSWAY, [Items.WAVE_BEAM]),
        ]
    ),
    Locations.CHOZO_CROSSWAY: Location(
        pickups=[ItemPickup(Items.MISSILE_EXPANSION, [Items.MORPH_BALL, Items.BOOST_BALL, Items.SPIDER_BALL])],
        doors=[
            Door(Locations.CHOZO_CROSSWAY_ACCESS_WEST),
            Door(Locations.CHOZO_CROSSWAY_ACCESS_SOUTH, [Items.ICE_BEAM]),
            Door(Locations.CHOZO_ELDER_HALL_ACCESS, [Items.SUPER_MISSILE, Items.MISSILES]),
        ]
    ),
    Locations.CHOZO_CROSSWAY_ACCESS_SOUTH: Location(
        doors=[
            Door(Locations.CHOZO_CROSSWAY, [Items.ICE_BEAM]),
            Door(Locations.CHOZO_HALL_OF_THE_ELDERS, [Items.ICE_BEAM]),
        ]
    ),
    Locations.CHOZO_ELDER_HALL_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_CROSSWAY),
            Door(Locations.CHOZO_HALL_OF_THE_ELDERS),
        ]
    ),
    Locations.CHOZO_HALL_OF_THE_ELDERS: Location(
        pickups=[ItemPickup(Items.ENERGY_TANK)],
        doors=[
            Door(Locations.CHOZO_EAST_FURNACE_ACCESS, [Items.ICE_BEAM, Items.MORPH_BALL]),
            Door(Locations.CHOZO_ELDER_CHAMBER),
            Door(Locations.CHOZO_CROSSWAY_ACCESS_SOUTH),
            Door(Locations.CHOZO_ELDER_HALL_ACCESS),
            Door(Locations.CHOZO_REFLECTING_POOL_ACCESS),
        ]
    ),
    Locations.CHOZO_ELDER_CHAMBER: Location(
        pickups=[ItemPickup(Items.ARTIFACT_WILD)],
        doors=[Door(Locations.CHOZO_HALL_OF_THE_ELDERS)]
    ),
    # Reflecting Pool / Transporters
    Locations.CHOZO_REFLECTING_POOL_ACCESS: Location(
        doors=[
            Door(Locations.CHOZO_HALL_OF_THE_ELDERS),
            Door(Locations.CHOZO_REFLECTING_POOL),
        ]
    ),
    Locations.CHOZO_REFLECTING_POOL: Location(
        doors=[
            Door(Locations.CHOZO_REFLECTING_POOL_ACCESS),
            Door(Locations.CHOZO_ANTECHAMBER, [Items.MISSILES]),
            Door(Locations.CHOZO_SAVE_STATION_3),
            Door(Locations.CHOZO_TRANSPORT_ACCESS_SOUTH),
        ]
    ),
    Locations.CHOZO_ANTECHAMBER: Location(
        pickups=[ItemPickup(Items.ICE_BEAM)],
        doors=[Door(Locations.CHOZO_REFLECTING_POOL, [Items.ICE_BEAM])]
    ),
    Locations.CHOZO_SAVE_STATION_3: Location(
        doors=[
            Door(Locations.CHOZO_REFLECTING_POOL),
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_EAST),
        ]
    ),
    Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_EAST: Location(
        doors=[Door(Locations.CHOZO_SAVE_STATION_3)]
    ),
    Locations.CHOZO_TRANSPORT_ACCESS_SOUTH: Location(
        doors=[
            Door(Locations.CHOZO_REFLECTING_POOL, [Items.ICE_BEAM]),
            Door(Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_SOUTH),
        ]
    ),
    Locations.CHOZO_TRANSPORT_TO_TALLON_OVERWORLD_SOUTH: Location(
        doors=[Door(Locations.CHOZO_TRANSPORT_ACCESS_SOUTH)]
    ),
}



