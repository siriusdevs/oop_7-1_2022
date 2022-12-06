"""Variables and objects for tests."""
from building_map import Building, Map

# Building variables

BUILD1 = {
    'obj': Building(50, 10, 12, (1, 5)),
    'dict': {
        'height': 50,
        'area': 10,
        'floors': 12,
        'location': (1, 5)
    },
    'str': 'Height: 50, area: 10, floors: 12\nLocation: (1, 5)'
}

BUILD2 = {
    'obj': Building(10, 5, 5, (3, 4)),
    'dict': {
        'height': 10,
        'area': 5,
        'floors': 5,
        'location': (3, 4)
    },
    'str': 'Height: 10, area: 5, floors: 5\nLocation: (3, 4)'
}

BUILD3 = {
    'obj': Building(150, 50, 18, (2, 8)),
    'dict': {
        'height': 150,
        'area': 50,
        'floors': 18,
        'location': (2, 8)
    },
    'str': 'Height: 150, area: 50, floors: 18\nLocation: (2, 8)'
}

# Map variables


def to_str(given_map: dict) -> list:
    """String representation of the attribute map and buildings.

    Args:
        given_map : dict - map that must be converted to string
    """
    full_map = '\n'.join([str(line) for line in given_map['map_list']])
    all_buildings = '\n'.join(['{0}:\n{1}'.format(key, building) for key, building in given_map['builds'].items()])
    return [full_map, all_buildings]


MAP1_A = {
    'map_list': [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ],
    'builds': {
        'building0': 'Height: 8, area: 3, floors: 4\nLocation: (1, 2)',
        'building2': 'Height: 20, area: 12, floors: 10\nLocation: (4, 4)'
    }
}
MAP1 = {
    'obj': Map(4, 6, MAP1_A['map_list'], MAP1_A['builds']),
    'dict': {
        'length': 4,
        'width': 6,
        'map_list': MAP1_A['map_list'],
        'buildings': MAP1_A['builds']
    },
    'str': 'Scale: 4x6\n{0}\nBuildings on map:\n{1}'.format(*to_str(MAP1_A))
}

MAP2_A = {
    'map_list': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    'builds': {
        'building3': 'Height: 45, area: 30, floors: 5\nLocation: (4, 3)',
        'building1': 'Height: 10, area: 5, floors: 4\nLocation: (8, 5)'
    }
}
MAP2 = {
    'obj': Map(10, 5, MAP2_A['map_list'], MAP2_A['builds']),
    'dict': {
        'length': 10,
        'width': 5,
        'map_list': MAP2_A['map_list'],
        'buildings': MAP2_A['builds']
    },
    'str': 'Scale: 10x5\n{0}\nBuildings on map:\n{1}'.format(*to_str(MAP2_A))
}

MAP3_A = {
    'map_list': [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    'builds': {
        'building4': 'Height: 23, area: 5, floors: 5\nLocation: (1, 3)',
        'building5': 'Height: 19, area: 9, floors: 8\nLocation: (3, 1)'
    }
}
MAP3 = {
    'obj': Map(7, 3, MAP3_A['map_list'], MAP3_A['builds']),
    'dict': {
        'length': 7,
        'width': 3,
        'map_list': MAP3_A['map_list'],
        'buildings': MAP3_A['builds']
    },
    'str': 'Scale: 7x3\n{0}\nBuildings on map:\n{1}'.format(*to_str(MAP3_A))
}
