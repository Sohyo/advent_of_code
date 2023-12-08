import re


def read_file_by_line(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_max_num_of_colour_cube(str_line, colour):
    my_regex = r'\d+?(?= '+re.escape(colour)+r")"   # r"\d+?(?= colour)" for using variable in re
    max_num = re.findall(my_regex, str_line)  # get the maximum num in each colour
    max_num = [int(element) for element in max_num] # chance str to int to use max()
    return max(max_num)


def get_num_of_colour_cube(str_line, colour):
    my_regex = r'\d+?(?= ' + re.escape(colour) + r")"  # r"\d+?(?= colour)" for using variable in re
    return int(re.search(my_regex, str_line).group())


# get input - Game and cubes
text_input = "test1.txt"
input_lines = read_file_by_line(text_input)

game_dictionary = {}
colours_cubes = ['blue', 'green', 'red']
for line in input_lines:
    game_num = int(re.search(r'\d+?(?=:)', line).group())   # get the number of the Game
    game_dictionary[game_num] = {colour: get_max_num_of_colour_cube(line, colour) for colour in colours_cubes}

# Now Elf will ask a question
elf = "12 red, 13 green, 14 blue, possible or impossible he??"
elf_dictionary = {}
for colour in colours_cubes:
    elf_dictionary[colour] = get_num_of_colour_cube(elf, colour)

# Check
result = 0
for game_num, game_colours in game_dictionary.items():
    if not any(game_colours[colour] > elf_dictionary[colour] for colour in colours_cubes):
        result += game_num

### Part 2 ###

part2_final_result = 0
for game in game_dictionary.values():
    multiply_cube_nums = 1
    for cube in game.values():
        multiply_cube_nums *= cube
    part2_final_result += multiply_cube_nums
print(part2_final_result)


## another option :P

from math import prod
sum(prod(max_cube_per_color.values()) for max_cube_per_color in game_dictionary.values())