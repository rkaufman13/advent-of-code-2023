from numpy import diff
from utils import file_parsing
from functools import reduce

list_of_lists = []

def find_offset_backwards(lists):
    offsets = [i[0] for i in lists]
    total_offset = 0
    if len(offsets)==1:
        return offsets[0]
    if len(offsets) ==2:
        return (offsets[1]-offsets[0])*-1
    offsets=offsets[::-1]
    total_offset = offsets[1]-offsets[0]
    for i in range(2, len(offsets)):
        total_offset= offsets[i] - total_offset
    return total_offset

def find_offset(lists):
    offsets = [i[-1] for i in lists]
    offset = reduce(lambda a,b: a+b, offsets)
    return offset

def find_differences_backwards(num_list, difference):
    first_diffs = []
    done = False
    global list_of_lists
    for index, number in enumerate(num_list):
        if index >0:
            first_diffs.append(number-num_list[index-1])
    list_of_lists.append(first_diffs)
    if len(set(first_diffs))<=1:
        done=True
        difference = find_offset_backwards(list_of_lists)
        list_of_lists = []
    else:
        return find_differences_backwards(first_diffs, difference)
    return first_diffs, done, difference

def find_differences(num_list, difference):
    first_diffs = []
    done = False
    global list_of_lists
    for index, number in enumerate(num_list):
        if index >0:
            first_diffs.append(number-num_list[index-1])
    list_of_lists.append(first_diffs)
    if len(set(first_diffs))<=1:
        done=True
        difference = find_offset(list_of_lists)
        list_of_lists = []
    else:
        return find_differences(first_diffs, difference)
    return first_diffs, done, difference

def part_one():
    path ="day9/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    for line in data:
        original_values = [int(num) for num in line.replace("\n","").split()]
        list_of_numbers = list(original_values)
        list_of_numbers, done, offset = find_differences(list_of_numbers, 0)
        if done:
            first_num = original_values[-1]
            total+=(first_num+offset)
    print(total)      



def part_two():
    path ="day9/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    for line in data:
        original_values = [int(num) for num in line.replace("\n","").split()]
        list_of_numbers = list(original_values)
        list_of_numbers, done, offset = find_differences_backwards(list_of_numbers, 0)
        if done:
            first_num = original_values[0]
            total+=(first_num-offset)
    print(total)      


#part_one()
part_two()