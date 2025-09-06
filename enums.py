from enum import Enum, auto

class Items(Enum):
    # Movement
    MORPH_BALL = auto()
    BOMBS = auto()
    BOOST_BALL = auto()
    SPIDER_BALL = auto()
    SPACE_BOOTS = auto()
    GRAPPLE_BEAM = auto()


    # Fighting
    MISSILES = auto()
    POWER_BOMB = auto()
    SUPER_MISSILE = auto()
    PLASMA_BEAM = auto()
    CHARGE_BEAM = auto()
    WAVE_BEAM = auto()
    ICE_BEAM = auto()

    XRAY_VISOR = auto()
    THERMAL_VISOR = auto()

    VARIA_SUIT = auto()
    GRAVITY_SUIT = auto()

    MISSILE_EXPANSION = auto()
    ENERGY_TANK = auto()



class GameEvents(Enum):
    HIVE_MECHA_DEFEATED = auto()
    FLAAHGRA_DEFEATED = auto()