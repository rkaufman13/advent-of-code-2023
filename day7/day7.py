from utils import file_parsing

card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def sort_hand(hand):
    return "".join(sorted(hand))

def day_one():
    path="day7/input/sample_data.txt"
    data = file_parsing.open_and_read_file(path)
    for line in data:
        line = line.split()
        bid = line[1]
        hand=line[0]
        hand = sort_hand(hand)
        

day_one()