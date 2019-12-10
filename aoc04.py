def check_password(password):
    string_password = str(password)
    password_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    # Check to make sure increasing order
    part_1 = 0
    part_2 = 0    
    if string_password[1] >= string_password[0] and string_password[2] >= string_password[1] and string_password[3] >= string_password[2] and string_password[4] >= string_password[3] and string_password[5] >= string_password[4]:
        dummy = True
    else:
        return [part_1, part_2]

    # Check at least two digits the same
    if string_password[0] == string_password[1] or string_password[1] == string_password[2] or string_password[2] == string_password[3] or string_password[3] == string_password[4] or string_password[4] == string_password[5]:
        part_1 = 1
        # Now count number of repeated digits for part 2
        password_dict[string_password[0]] += 1
        password_dict[string_password[1]] += 1
        password_dict[string_password[2]] += 1
        password_dict[string_password[3]] += 1
        password_dict[string_password[4]] += 1
        password_dict[string_password[5]] += 1
        counts = password_dict.values()
        if 2 in counts:
            part_2 = 1    
    return [part_1, part_2]

start_range = 206938
end_range = 679128
part_1 = 0
part_2 = 0

for password in range(start_range, end_range + 1):
    result = check_password(password)
    part_1 += result[0]
    part_2 += result[1]
    
print('Part 1: ' + str(part_1))
print('Part 2: ' + str(part_2))


