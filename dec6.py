with open("dec6.txt", "r") as input_file:
    input_data = input_file.read().split("\n\n")
    

# Part one
input_data_pt1 = [line.replace("\n", "") for line in input_data]
print(sum([len(set(line)) for line in input_data_pt1]))

# Part two
input_data_pt2 = [[set(individual) for individual in group.split()] for group in input_data]
print(sum([len(set.intersection(*group)) for group in input_data_pt2]))