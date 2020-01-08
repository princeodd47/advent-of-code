def write_list_to_file(in_list, out_file_name):
    with open(out_file_name, 'w') as out_file:
        for i in in_list:
            out_file.write("{}\n".format(i))

def write_str_to_file(in_str, out_file_name):
    with open(out_file_name, 'w') as out_file:
        out_file.write("{}\n".format(in_str))

def get_file(in_file_name):
    with open(in_file_name) as in_file:
        data = in_file.readlines()
    return data

def same_letter_diff_case(cha_a, cha_b):
    if cha_a.lower() == cha_b.lower() and cha_a != cha_b:
        return True
    else:
        return False

def activate_reaction(in_list):
    for i in range(0, len(in_list)):
        if i < len(in_list)-1:
            if same_letter_diff_case(in_list[i], in_list[i+1]):
                #print("found: {}:{} {}:{}".format(
                #    i, in_list[i], i+1, in_list[i+1])
                #)
                del in_list[i+1]
                del in_list[i]
                return in_list
    return in_list

data = get_file("input.txt")
#data = get_file("input_small.txt")
polymers = list(data[0].rstrip())

reaction_found = True
counter = 0
while reaction_found:
    #print("counter: {} : ".format(counter), end="")
    #print("counter: {} : {}".format(counter, polymers))
    orig_length = len(polymers)
    polymers = activate_reaction(polymers)
    new_length = len(polymers)
    #print("orig: {} new: {}".format(orig_length, new_length))
    if orig_length == new_length:
        reaction_found = False
    counter += 1

print(len(polymers))
polymers_str = ''.join(polymers)
write_str_to_file(polymers_str, "polymers_reacted")
