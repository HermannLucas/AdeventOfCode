def filter_units(first_unit, second_unit):
    if first_unit.casefold() == second_unit.casefold() and first_unit != second_unit:
        return True
    return False

def filter_directions(first_unit, second_unit):
    if first_unit.casefold() == second_unit.casefold() and first_unit != second_unit:
        return False
    return True

def recurse(directions):
    filtered = []

    try:
        for index, direction in enumerate(directions):
            if filter_directions(direction, directions[index + 1]):
                filtered.append(direction)
            else:
                filtered.extend(directions[index + 2:])
                return recurse(filtered)
    except IndexError:
        return directions

def recurse_problem1(directions):
    return len(recurse(directions))

def problem1(polymer):
    return len(polymerReduc(polymer))

def polymerReduc(polymer):
    new_polymer = []
    for unit in polymer:
        if new_polymer and filter_units(unit, new_polymer[-1]):
            new_polymer.pop()
        else:
            new_polymer.append(unit)
    return new_polymer

def problem2(polymer):
    return min([len(polymerReduc(polymer.replace(unit, "").replace(unit.swapcase(), ""))) for unit in set(polymer.lower())])
