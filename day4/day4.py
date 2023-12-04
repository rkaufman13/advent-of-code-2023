from utils import file_parsing
import re

def find_dupes(list):
    seen = set()
    dupes = []

    for x in list:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    return dupes

def preprocess(line, cards):
    line = line.split(":")
    card_name = re.search("\d+", line[0]).group(0)
    winning_numbers = line[1].split("|")[0].split()
    have_numbers = line[1].split("|")[1].split()
    cards.append({'card': int(card_name), 'winning':winning_numbers, 'have':have_numbers})
    return cards

def preprocess_as_object(line, cards):
    line = line.split(":")
    card_name = int(re.search("\d+", line[0]).group(0))
    winning_numbers = line[1].split("|")[0].split()
    have_numbers = line[1].split("|")[1].split()
    cards[card_name]={'card': card_name, 'winning':winning_numbers, 'have':have_numbers, 'quantity': 1}
    return cards
    


def part_one():
    path="day4/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total=0
    cards = []
    for line in data:
        cards = preprocess(line, cards)
    for card in cards:
        all_numbers = []
        all_numbers.extend(card['have'])
        all_numbers.extend(card['winning'])
        duplicates = find_dupes(all_numbers)
        if len(duplicates) == 1:
            card['value']=1
        elif len(duplicates)>1:
            card['value']=2**(len(duplicates)-1)
        else:
            card['value']=0
        total+=card['value']
    print(total)

def part_two():
    path="day4/input/full_data.txt"
    data = file_parsing.open_and_read_file(path)
    total=0
    cards = {}
    for line in data:
        cards = preprocess_as_object(line, cards)
    for card in cards:
        all_numbers = []
        all_numbers.extend(cards[card]['have'])
        all_numbers.extend(cards[card]['winning'])
        duplicates = find_dupes(all_numbers)
        if len(duplicates):
            for i in range(1, len(duplicates)+1):
                desired_card = cards[card+i]
                desired_card['quantity']+=1*cards[card].get("quantity",1)
    for card in cards:
        
        total+=cards[card].get("quantity",0)
    print(total)

part_one()
part_two()