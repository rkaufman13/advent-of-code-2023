from utils import file_parsing
from functools import reduce

requirements = {'red':12, 'green':13, 'blue':14}

def preprocess(data):
    processed_dict={}
    
    for row in data:
        processed_row ={}
        row = row.replace("\n","")
        row = row.split(": ")
        game = row[0].split(" ")[1]
        row = row[1].split("; ")
        for pull_string in row:
            pull_string = pull_string.split(", ") #['3 blue', '4 red'] 
            for individual_pull in pull_string: #'3 blue'
                pull = individual_pull.split(" ") #['3','blue']
                color = pull[1]
                count = int(pull[0])
                if( processed_row.get(color) and count> processed_row.get(color)) or not processed_row.get(color):
                    processed_row[color] = count
            processed_dict[game] = processed_row
    return processed_dict

def part_one():
    path ="day2/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    processed_dict = preprocess(data)
    possible_games = {}
    for k,v in processed_dict.items():
        for color, count in v.items():
            if count>requirements[color]:
                if possible_games.get(int(k)):
                    del(possible_games[int(k)])
                break
            else:
               possible_games[int(k)] = True
    total = sum(possible_games.keys())
    print(total)

def part_two():
    path ="day2/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    processed_dict = preprocess(data)
    min_cubes_set = processed_dict.values()
    total=0
    for set in min_cubes_set:
        total+=reduce(lambda a, b: a*b, set.values())
    print(total)

part_one()
part_two()