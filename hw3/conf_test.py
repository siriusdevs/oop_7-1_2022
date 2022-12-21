"""Variables and objects for tests."""
from building_map import Building, Map

# Building variables

BUILD1 = {
    'obj': Building(50, 10, 12, [1, 5]),
    'dict': {
        'height': 50,
        'area': 10,
        'floors': 12,
        'location': [1, 5]
    },
    'str': 'Height: 50, area: 10, floors: 12\nLocation: [1, 5]'
}

BUILD2 = {
    'obj': Building(10, 5, 5, [3, 4]),
    'dict': {
        'height': 10,
        'area': 5,
        'floors': 5,
        'location': [3, 4]
    },
    'str': 'Height: 10, area: 5, floors: 5\nLocation: [3, 4]'
}

BUILD3 = {
    'obj': Building(150, 50, 18, [2, 8]),
    'dict': {
        'height': 150,
        'area': 50,
        'floors': 18,
        'location': [2, 8]
    },
    'str': 'Height: 150, area: 50, floors: 18\nLocation: [2, 8]'
}

# Map variables


def to_str(given_map: dict) -> list:
    """String representation of the attribute map and buildings.

    Args:
        given_map : dict - map that must be converted to string
    """
    full_map = '\n'.join([str(line) for line in given_map['map_list']])
    all_buildings = '\n'.join(['{0}:\n{1}'.format(key, building) for key, building in given_map['builds_str'].items()])
    return [full_map, all_buildings]


MAP1_A = {
    'map_list': [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ],
    'builds': {
        'building0': 'test_buildings/building0.json',
        'building2': 'test_buildings/building2.json'
    },
    'builds_str': {
        'building0': 'Height: 8, area: 3, floors: 4\nLocation: [1, 2]',
        'building2': 'Height: 20, area: 12, floors: 10\nLocation: [3, 3]'
    }
}
MAP1 = {
    'obj': Map(4, 6, MAP1_A['builds']),
    'dict': {
        'length': 4,
        'width': 6,
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
        'building3': 'test_buildings/building3.json',
        'building1': 'test_buildings/building1.json'
    },
    'builds_str': {
        'building3': 'Height: 45, area: 30, floors: 5\nLocation: [4, 2]',
        'building1': 'Height: 10, area: 5, floors: 4\nLocation: [7, 4]'
    }
}
MAP2 = {
    'obj': Map(10, 5, MAP2_A['builds']),
    'dict': {
        'length': 10,
        'width': 5,
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
        'building4': 'test_buildings/building4.json',
        'building5': 'test_buildings/building5.json'
    },
    'builds_str': {
        'building4': 'Height: 23, area: 5, floors: 5\nLocation: [0, 2]',
        'building5': 'Height: 19, area: 9, floors: 8\nLocation: [2, 0]'
    }
}
MAP3 = {
    'obj': Map(7, 3, MAP3_A['builds']),
    'dict': {
        'length': 7,
        'width': 3,
        'buildings': MAP3_A['builds']
    },
    'str': 'Scale: 7x3\n{0}\nBuildings on map:\n{1}'.format(*to_str(MAP3_A))
}
