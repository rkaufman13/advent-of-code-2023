import re
from functools import reduce
from utils import file_parsing

def find_whole_number(string, index):
     result = re.findall("\d+", string)
     if len(result)>1 and index >1:
          return result[1]
     return result[0]

def get_num_positions(line):
    numbers = re.findall('\d+', line)
    starting_indices=[]
    if len(numbers):
        for number in numbers:
            position = re.search(f"(?!\D){str(number)}(?=\D)", line)
            blank_spaces = "x"*len(number)
            line = line[:position.start()] + blank_spaces + line[position.end():]
            starting_indices.append({"start":position.start(), "end": position.end()-1, "value":int(number)})
    return starting_indices    

def get_gear_positions(line):
    gears = re.findall('\*', line)
    starting_indices=[]
    if len(gears):
        for gear in gears:
            index = line.find("*")
            if index>=0:
                line = line[:index] + "x" + line[index+1:]
                starting_indices.append(index)
    return starting_indices    


def check_for_matches_left_right(number, index, data):
    curr_line = data[index]
    if not re.match("\.", curr_line[number['start']-1]):
                number["include"]= True
    if number['end']<len(curr_line):
            if not re.match("\.|\n", curr_line[number['end']+1]):
                number["include"] = True
    return number


def check_for_matches_below(number, index, data):
    if index==len(data)-1:
        return number         
    below_line = data[index+1]
    for i in range(number['start']-1,number['end']+2):
            if i<0:
                 pass
            elif not re.match("\.|\d|\n", below_line[i]):
                number["include"]=True 
    return number

def check_for_gear_matches_above_below(gear, index, data, parts, offset):
    if index==len(data)-1 or index<0:
        return parts         
    line_to_check = data[index+offset]
    value = None
    if re.match("\d", line_to_check[gear-1]) or re.match("\d", line_to_check[gear]):
            value = find_whole_number(line_to_check[max(gear-3,0):gear+3], 0)
    elif re.match("\d", line_to_check[gear+1]):
            value = find_whole_number(line_to_check[gear+1:gear+4], 1)
            
    if value:
        parts.append(value)
    return parts

def check_for_matches_above(number, index, data):
    if index==0:
         return number
    above_line = data[index-1]
    for i in range(number['start']-1,number['end']+2):
            if i<0:
                 pass
            elif not re.match("\.|\d|\n", above_line[i]):
                number["include"]=True
    return number

def check_for_matches(number, index, data):
    number = check_for_matches_above(number, index, data)
    number = check_for_matches_left_right(number, index, data)
    number = check_for_matches_below(number, index,data)
    return number

def check_for_gear_matches(gear, index, data):
    parts = []
    parts = check_for_gear_matches_above_below(gear, index, data, parts, -1)
    # parts = check_for_gear_matches_left_and_right(gear, index, data)
    parts = check_for_gear_matches_above_below(gear, index, data, parts, 1)
    return parts

def part_one():
    path ="day3/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    for index, line in enumerate(data):
        data[index] = "."+line
    for index, line in enumerate(data):
        processed_line = get_num_positions(line)
        for number in processed_line:
            number=check_for_matches(number, index, data)
            if number.get("include"):
                total+=number.get("value")
    print(total)

def part_two():
    path ="day3/input/sample_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    for index, line in enumerate(data):
        data[index] = "."+line
    for index, line in enumerate(data):
         processed_line = get_gear_positions(line)
         parts = []
         for gear in processed_line:
              parts = check_for_gear_matches(gear, index, data)
         if len(parts)>=2:
            total+= reduce(lambda a, b: int(a)*int(b), parts)
    print(total)
#part_one()

part_two()