import random

lines_file = open('./player_names.txt', 'r')
player_names = lines_file.readlines()
temp_list = []
for player_name in player_names:
    temp_list.append(str(player_name).rstrip("\n"))
player_names = temp_list
lines_file.close()

randomized_names = player_names
random.shuffle(randomized_names)

lines_file = open('./player_roles.txt', 'r')
player_roles = lines_file.readlines()
temp_list = []
for player_role in player_roles:
    temp_list.append(str(player_role).rstrip("\n"))
player_roles = temp_list
lines_file.close()

formatted_output = []
for line in player_roles:
    temp_list = line.split(",")
    if len(player_names) >= int(temp_list[2]):
        range_end = int(temp_list[1])
        for i in range(0, range_end):
            rn = str(randomized_names.pop())
            rr = str(temp_list[0])
            formatted_output.append("/message " + rn + " You have been assigned the following role: " + rr)

output_file = open('./formatted_output.txt', 'w')
for line in formatted_output:
    output_file.write(line + '\n')

output_file.close()
