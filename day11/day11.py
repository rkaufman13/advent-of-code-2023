from utils import file_parsing
from itertools import permutations
from more_itertools import distinct_permutations


def expand_the_universe(universe):
    new_universe = []
    for i in range(0, len(universe)):
        new_universe.append(universe[i])
        if '#' not in universe[i]:
            new_universe.append(universe[i])
    update_has_happened = False
    for i in range(0, 10000000):
        try:
            universe_slice = list(part[i] for part in new_universe)
        except IndexError:
            break  # this is evil and I love it
        if '#' not in universe_slice and not update_has_happened:
            update_has_happened = True
            for j in range(0, len(new_universe)):
                new_universe[j] = new_universe[j][:i + 1] + '.' + new_universe[j][i + 1:]
        elif update_has_happened:
            update_has_happened = False

    return new_universe


def expand_the_universe_metaphorically(universe):
    xes = []
    ys = []
    for i in range(0, len(universe)):
        if '#' not in universe[i]:
            ys.append(i)
    rotated_universe = list(zip(*universe[::-1]))
    for j in range(0, len(rotated_universe)):
        if '#' not in rotated_universe[j]:
            xes.append(j)
    return xes, ys


def find_galaxies(universe):
    all_galaxies = []
    for row in range(len(universe)):
        for col in range(len(universe[0])):
            if universe[row][col] == '#':
                all_galaxies.append({'x': col, 'y': row})
    return all_galaxies


def day_one():
    path = "input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    universe = expand_the_universe(data)
    for slice in universe:
        print(slice)
    galaxies = find_galaxies(universe)

    total = 0
    all_permutations = permutations(galaxies, 2)
    done = []

    for combo in all_permutations:
        print(combo)
        if (combo[1], combo[0]) not in done:
            distance = abs(combo[0]['x'] - combo[1]['x']) + abs(combo[0]['y'] - combo[1]['y'])
            total += distance
            done.append(combo)
    print(total)


def day_two():
    path = "input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    universe = list(data)
    xes, ys = expand_the_universe_metaphorically(data)
    galaxies = find_galaxies(universe)

    total = 0
    all_permutations = permutations(galaxies, 2)
    done = []

    for combo in all_permutations:
        if (combo[1], combo[0]) not in done:
            start_x = min(combo[0]['x'], combo[1]['x'])
            end_x = max(combo[0]['x'], combo[1]['x'])
            start_y = min(combo[0]['y'], combo[1]['y'])
            end_y = max(combo[0]['y'], combo[1]['y'])
            millions = sum(start_x < num < end_x for num in xes) + sum(start_y < num < end_y for num in ys)
            distance = abs(combo[0]['x'] - combo[1]['x']) + abs(combo[0]['y'] - combo[1]['y'])+ millions*999999
            total += distance
            done.append(combo)
    print(total)


# day_one()

day_two()
