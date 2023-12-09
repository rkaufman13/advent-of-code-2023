from utils import file_parsing
import re

def navigate_maze(directions, maps, starting_key, steps):
    for direction in directions:
        steps+=1
        result = maps[starting_key][int(direction)]
        if result == 'ZZZ':
            return steps
        starting_key = result
    if result != 'ZZZ':
        steps = navigate_maze(directions, maps, result, steps)        
    return steps


def navigate_maze_more_better(directions, maps, starting_keys, steps):
    for direction in directions:
        steps+=1
        for index, key in enumerate(starting_keys):
            result = maps[key][int(direction)]
            starting_keys[index] = result
        if all(key[2]=='Z' for key in starting_keys):
            return steps
    if all(key[2]=='Z' for key in starting_keys):
            return steps
    else:
        steps = navigate_maze_more_better(directions, maps, starting_keys, steps)        
    return steps



def part_one():
    path ="day8/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)

    directions = data.pop(0).replace("L",'0').replace("R",'1').replace("\n","")
    data.pop(0)
    maps = {}
    for line in data:
        line = line.split(" = ")
        maps[line[0]] =  re.findall("\w+", line[1])
    steps = navigate_maze(directions,maps, "AAA", 0)
    print(steps)

def part_two():
    path ="day8/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)

    directions = data.pop(0).replace("L",'0').replace("R",'1').replace("\n","")
    data.pop(0)
    maps = {}
    starting_nodes =[]
    for line in data:
        line = line.split(" = ")
        maps[line[0]] =  re.findall("\w+", line[1])
        if re.match("\w\wA", line[0]):
            starting_nodes.append(line[0])
    steps = navigate_maze_more_better(directions,maps, starting_nodes, 0)
    print(steps)


#part_one()

part_two()