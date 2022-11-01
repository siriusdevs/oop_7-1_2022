"""Dynamic class creation test."""
from dynamic_class import create_class
from pytest import mark


def initializer(self, name: str, age: int):
    """A simple initializer for Human classes used in tests."""
    self.age = age
    self.name = name


tests = [({'__init__': initializer, 'planet': 'Earth'}, 'Ivan', 20),
         ({'__init__': initializer}, 'Mathway', 18)
         ]


@mark.parametrize('obj_data, name, age', tests)
def test_dynamic_classes(obj_data: dict, name: str, age: int):
    """Tests each created Human, one by one. Accumulates errors to assert them.

    Args:
        obj_data : dict - methods and attributes for class.
        name : str - a name of a human.
        age : int - an age of a human.
    """
    errors = []
    human = create_class('Human', obj_data)
    new_human = human(name, age)
    for key in obj_data.keys():
        if not key.startswith('__'):
            if getattr(new_human, key) != obj_data[key]:
                errors.append('Failed passing attributes and methods as keywords.')
    if new_human.name != name or new_human.age != age:
        errors.append('Failed initializing an object properly.')
    assert not errors, 'Errors occured: {0}'.format(' '.join(errors))
