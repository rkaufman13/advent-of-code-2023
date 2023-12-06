from utils import file_parsing
import re, functools


def find_winning_options(race):
    time=race['time']
    distance=race['distance']
    winning_options=0
    for i in range(time):
        if (time-i)*i>distance:
            winning_options+=1
    return winning_options

def part_two():
    race={'time': 51926890, 'distance': 222203111261225}
    
    winning_options = []
    winning_options_for_race = find_winning_options(race)
    winning_options.append(winning_options_for_race)
    print(winning_options)


def part_one():
    path="day6/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    times = re.findall("\d+", data[0])
    distances = re.findall("\d+", data[1])
    races = []
    for index, time in enumerate(times):
        races.append({'time': int(time), 'distance': int(distances[index])})
    
    winning_options = []
    for race in races:
        winning_options_for_race = find_winning_options(race)
        winning_options.append(winning_options_for_race)
    

    total = functools.reduce(lambda x, y: x*y, winning_options)
    print(total)
part_one()


part_two()