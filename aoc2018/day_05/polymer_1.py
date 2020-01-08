import string

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

data = get_file("polymers_reacted")
#data = get_file("input_small.txt")
#polymers = list(data[0].rstrip())
polymers = data[0].rstrip()

counter = 0
alphabet = string.ascii_lowercase
#alphabet = ['a']
polymers_backup = polymers
for i in alphabet:
    reaction_found = True
    polymers = polymers_backup
    #substitute all i from polymers
    #print(len(polymers))
    polymers = polymers.replace(i.lower(), "")
    #print(len(polymers))
    polymers = polymers.replace(i.upper(), "")
    #print(len(polymers))
    polymers_list = list(polymers)
    orig_length = len(polymers_list)
    while reaction_found:
        prev_length = len(polymers_list)
        polymers_list = activate_reaction(polymers_list)
        new_length = len(polymers_list)
        if prev_length == new_length:
            reaction_found = False
    print("{}: {} -> {}".format(i, orig_length, new_length))
