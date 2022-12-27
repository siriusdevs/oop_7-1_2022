from main import Buildings
from random import choice
import pytest
import os

shop = {(0, 0): 'shop'}
s5 = [5, 5, 5, 5, 5, 5]
s57 = [5, 5, 7, 7, 7, 5]
s0 = (0, 0)
p1 = [0, 0, 0, 2, 3, 7, 1, 6, 9]
exmap = []
for _ in range(6):
    exmaplist = []
    for _ in range(4):
        exmaplist.append(choice(p1))
    exmap.append(exmaplist)
exdict = {}
for i in enumerate(range(len(exmap))):
    for j in enumerate(range(len(exmap[0]))):
        if exmap[i[0]][j[0]]:
            exdict[(j[0], i[0])] = choice(["house", "shop"])
build = Buildings()
tests = [(['G', 'Somemap', '55', '6'], None),\
         (['G', 'Somemap', '-55', '6'], ('Invalid arguments', False))
         ]


@pytest.mark.parametrize('inp, answ', tests)
def test_g_valid(inp, answ):
    """Testing the function of validating the arguments of the map generating function."""
    assert build.g_valid(inp) == answ


tests = [(['O', 'i3onmjt'], None),\
         (['O'], ('Invalid arguments', False))
         ]


@pytest.mark.parametrize('inp, answ', tests)
def test_o_valid(inp, answ):
    """Testing the function of validating the arguments of the map importing function."""
    assert build.o_valid(inp) == answ


tests = [
    (['E', '0', '0', '1', '3', '3', 'shop'], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], None),
    (
        ['E', '0', '0', '1', '5', '3', 'shop'],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ('Invalid arguments', False)
    )
]


@pytest.mark.parametrize('inp, bmap, answ', tests)
def test_e_valid(inp, bmap, answ):
    """Testing the function of validating the arguments of the map editing function."""
    assert build.e_valid(inp, bmap) == answ


tests = [(['I', '0', '0'], shop, None),\
         (['I', '0', '1'], shop, ("Nothing", False))
         ]


@pytest.mark.parametrize('inp, b_type, answ', tests)
def test_i_valid(inp, b_type, answ):
    """Testing the function of validating the arguments of the building's type showing function."""
    assert build.i_valid(inp, b_type) == answ


tests = [('3', '4', [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])]


@pytest.mark.parametrize('x, y, answ', tests)
def test_generate(x, y, answ):
    """Testing map generating function."""
    assert build.generate(x, y) == answ


tests = [(exmap, 'donttouchthismapplease', exdict)]


@pytest.mark.parametrize('bmap, name, b_t', tests)
def test_file(bmap, name, b_t):
    """Testing map exporting and importing function."""
    print(b_t, bmap)
    build.to_file(bmap, name, b_t)
    map2, b_t2 = build.from_file('donttouchthismapplease')
    assert (bmap, b_t) == (map2, b_t2)


exmap2 = [m[:] for m in exmap]
exmap2[2][0] = 17
exdict2 = exdict.copy()
exdict2[(0, 2)] = 'zoo. 1 by x and 1 by y, 17 floors hight.'
tests = [
    (
        ['0', '2', '3', '2', '1', 'zoo'],
        exmap,
        exdict,
        None,
        ('Do you want to build your buildings on top of the old ones?[y/n]', True, exdict)
    ),
    (
        ['0', '2', '1', '1', '17', 'zoo'],
        exmap,
        exdict,
        'y',
        (exmap2, True, exdict2)
    )
]


@pytest.mark.parametrize('inp, bmap, b_type, y_n, answ', tests)
def test_editing_map(inp, bmap, b_type, y_n, answ):
    """Testing map editing function."""
    assert build.editing_map(inp, bmap, b_type, y_n) == answ


tests = [
    (['G'], (None, None, None), None, None, ("Invalid arguments", False)),
    (
        ['G', 'donttouchthismapplease', '5', '4'],
        (None, None, None),
        None,
        None,
        ("Map donttouchthismapplease does already exist", False)
    ),
    (['G', 'Hay', '5', '6'], ([0], None, 'name'), True, None, ("Do you want to save your map? [y/n]", True)),
    (['O'], (None, None, None), None, None, ("Invalid arguments", False)),
    (
        ['O', 'donttouchthismapplease'],
        ([0], None, 'name'),
        True,
        None,
        ("Do you want to save your map? [y/n]", True)
    ),
    (
        ['O', 'nuon0goijmwe0fmovjesnhlkuig'],
        (None, None, None),
        None,
        None,
        ("Sorry, Map nuon0goijmwe0fmovjesnhlkuig is damaged or doesn't exist.", False)
    ),
    (
        ['E', '3', '2', '1', '2', '5', 'shop'],
        (None, None, None),
        None,
        None,
        ("sorry, Map isn't opened", False)
    ),
    (['S'], ([[1, 0]], shop, 'name'), True, None, ([[1, 0]], 'name', False, {(0, 0): 'shop'})),
    (['Q'], ([[1, 0]], shop, 'name'), True, None, ("Do you want to save it? [y/n]", True)),
    (['Q'], ([[1, 0]], shop, 'name'), True, 'y', None),
    (['D'], ([[1, 0]], shop, 'name'), True, None, ('There is no such map here', False)),
    (['I', '0', '0'], ([[1, 0]], shop, 'name'), True, None, ('shop', False))
]


@pytest.mark.parametrize('inp, bmap, edited, y_n, answ', tests)
def test_inp_analyz(inp, bmap, edited, y_n, answ):
    """Testing the input analyzing function."""
    assert Buildings(inp, bmap, edited, y_n).input_analys() == answ


a = ("Builds_donttouchthismapplease.json", "Builds_name.json")


@pytest.mark.parametrize('name', a)
def test_deleting(name):
    """Deleting testing maps."""
    os.remove(name)
