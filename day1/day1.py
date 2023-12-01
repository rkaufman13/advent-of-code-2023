from utils import file_parsing
import re
path ="day1/input/sample_data_2.txt"


def part_1():
    path = "day1/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for line in data:
        line_of_only_ints= [char for char in line if char in digits]
        if len(line_of_only_ints) ==1:
            line_of_only_ints.append(line_of_only_ints[0])
        total =  total+ int(line_of_only_ints[0]+line_of_only_ints[-1])
    print(total)


def check_for_matches(line, new_array):
    
    if len(line)>0:
        num = re.compile('^\d')
        one = re.compile('^one')
        two = re.compile('^two')
        three = re.compile('^three')
        four = re.compile('^four')
        five = re.compile('^five')
        six = re.compile('^six')
        seven = re.compile('^seven')
        eight = re.compile('^eight')
        nine = re.compile('^nine')

        if num.match(line):
            new_array.append(int(line[0]))
        elif one.match(line):
            new_array.append(1)
        elif two.match(line):
            new_array.append(2)
        elif three.match(line):
            new_array.append(3)
        elif four.match(line):
            new_array.append(4)
        elif five.match(line):
            new_array.append(5)
        elif six.match(line):
            new_array.append(6)
        elif seven.match(line):
            new_array.append(7)
        elif eight.match(line):
            new_array.append(8)
        elif nine.match(line):
            new_array.append(9)
        else:
            pass
        new_array = check_for_matches(line[1:], new_array)
    return new_array
    
def part_2():
    path="day1/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total = 0
    
    for line in data:        
        
        new_line = check_for_matches(line, [])
        
        if len(new_line)==1:
                total+= int(str(new_line[0])+str(new_line[0]))
        else:
                total+= int(str(new_line[0]) + str(new_line[-1]))
    print(total)
#part_1()
part_2()