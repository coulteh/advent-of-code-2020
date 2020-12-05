from itertools import tee, islice, chain

input_data = []

with open("dec5.txt", "r") as input_file:
    for line in input_file:
        input_data.append(line.strip())

def input_to_binary(data):
    return data.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")

def input_to_binary_tuple(data):
    binary_row = data.replace("F", "0").replace("B", "1")
    binary_col = data.replace("L", "0").replace("R", "1")
    return binary_row[:7], binary_col[-3:]

def binary_to_base10(binary_coords):
    return int(binary_coords[0], 2), int(binary_coords[1], 2)

def get_seat_id(coords):
    return coords[0] * 8 + coords[1]

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

# Part one
max_seat_id = 0
for line in input_data:
    binary_tuple = input_to_binary_tuple(line)
    seat_coords = binary_to_base10(binary_tuple)
    seat_id = get_seat_id(seat_coords)
    if seat_id > max_seat_id: max_seat_id = seat_id
print(max_seat_id)

# Part two
seat_numbers = {}
binary_seats = []
for line in input_data:
    binary_seats.append(int(input_to_binary(line), 2))

binary_seats.sort()
print("The answer is the number between the following:")
for prev, item, nxt in previous_and_next(binary_seats):
    if prev:
        if nxt:
            if not (item == prev+1 and item == nxt-1):
                print(item)