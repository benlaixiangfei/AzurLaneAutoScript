from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('D1')
MAP.shape = 'I8'
MAP.camera_data = ['D3', 'D6', 'F3', 'F6']
MAP.camera_data_spawn_point = ['D6']
MAP.map_data = """
    -- -- ++ -- -- ME ++ ++ ++
    -- ++ ++ Me -- -- ME -- --
    ++ ++ ++ -- ++ -- -- -- MB
    -- Me -- Me -- -- ME -- --
    -- -- MS -- __ MS ++ ++ ME
    ++ ++ ++ -- -- -- ++ ME --
    ++ -- SP -- MS -- -- -- ME
    ++ -- SP -- ++ ME -- ME --
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 4, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
MAP.spawn_data_loop = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['Z24', 'Nuremberg', 'Carabiniere']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = False
    # ===== End of generated config =====

    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (80, 255 - 24),
        'width': (0.9, 10),
        'prominence': 10,
        'distance': 35,
    }
    EDGE_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (255 - 24, 255),
        'prominence': 10,
        'distance': 50,
        'width': (0, 10),
        'wlen': 1000,
    }
    INTERNAL_LINES_HOUGHLINES_THRESHOLD = 40
    EDGE_LINES_HOUGHLINES_THRESHOLD = 40
    COINCIDENT_POINT_ENCOURAGE_DISTANCE = 1.5
    HOMO_EDGE_HOUGHLINES_THRESHOLD = 180
    MAP_ENEMY_GENRE_DETECTION_SCALING = {
        'DD': 1.111,
        'CL': 1.111,
        'CA': 1.111,
        'CV': 1.111,
        'BB': 1.111,
    }
    MAP_SWIPE_MULTIPLY = 1.579
    MAP_SWIPE_MULTIPLY_MINITOUCH = 1.527
    MAP_ENEMY_TEMPLATE = ['LightInvertedOrthant', 'MainInvertedOrthant', 'CarrierInvertedOrthant']


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_enemy(scale=(1,)):
            return True
        if self.clear_enemy(scale=(2,), genre=['LightInvertedOrthant', 'MainInvertedOrthant']):
            return True
        if self.clear_enemy(scale=(3,), genre=['LightInvertedOrthant', 'MainInvertedOrthant']):
            return True
        if self.clear_enemy(scale=(2,), genre=['Enemy', 'CarrierInvertedOrthant']):
            return True
        if self.clear_enemy(scale=(3,), genre=['Enemy', 'CarrierInvertedOrthant']):
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()
