# https://adventofcode.com/2018/day/4

import collections
import json
import re
import sys
import time

def get_file(in_file_name):
    with open(in_file_name) as in_file:
        data = in_file.readlines()
    return data

def write_dict_to_file(in_dict, out_file_name):
    with open(out_file_name, 'w') as out_file:
        out_file.write(json.dumps(in_dict))

def write_list_to_file(in_list, out_file_name):
    with open(out_file_name, 'w') as out_file:
        for i in in_list:
            out_file.write("{}\n".format(i))

def format_timestamp(in_time):
    time_split = in_time.split()
    date = re.sub('[\[-]', '', time_split[0])
    time = re.sub('[: ]', '', time_split[1])
    return int(date + time)

def print_dictionary(in_dict):
    n = 0
    for i in in_dict:
        for k in in_dict[i]:
            if n <= 10:
                print("{}: {}: {}".format(i, k, in_dict[i][k]))
            n += 1

def print_list(in_list):
    counter = 0
    for i in in_list:
        if counter < 10:
            print(i)
        counter += 1


def get_guard_ids(in_dict):
    guards = []
    for i in in_dict:
        for k in in_dict[i]:
            if k not in guards:
                guards.append(int(k))
    guards = set(guards)
    return guards

def initialize_guard_dict(in_list):
    out_dict = {}
    for i in in_list:
        out_dict.update({i:{}})
    return out_dict

def update_with_guard_ids_and_actions(in_dict):
    guard_id = 0
    for i in in_dict:
        for k in in_dict[i]:
            if '#' in in_dict[i][k]:
                val_split = in_dict[i][k].split()
                guard_id = re.sub('#', '', val_split[1])
            if 'begin' in in_dict[i][k]:
                action = "begin"
            elif 'asleep' in in_dict[i][k]:
                action = "asleep"
            elif 'wake' in in_dict[i][k]:
                action = "wake"
            in_dict.update({i: {guard_id: action}})
    return in_dict

in_file_name = "1204_input.txt"
out_file_name = "1204_1_out"
data = get_file(in_file_name)
log = {}

for line in data:
    line_split = line.split(']')
    timestamp = format_timestamp(line_split[0])
    log.update({timestamp: {'action': line_split[1]}})
    log_ordered = collections.OrderedDict(sorted(log.items()))

#write_dict_to_file(log_ordered, "log_ordered")

log_guard = update_with_guard_ids_and_actions(log_ordered)
#write_dict_to_file(log_guard, "log_guard")

# example guard_sleep dict
#guard_sleep = {
#        2543: {
#            1518022: {
#                15: 'asleep'
#                }
#            }
#        }

guard_list = get_guard_ids(log_guard)
write_list_to_file(guard_list, "1204_guard_list")


guard_sleep = {}
for timestamp in log_guard:
    timestamp_str = str(timestamp)
    date_str = timestamp_str[:-4]
    time_str = timestamp_str[-4:]
    date_int = int(date_str)
    for guard_id in log_guard[timestamp]:
        if guard_id not in guard_sleep:
            guard_sleep.update({guard_id: collections.OrderedDict({timestamp: log_guard[timestamp][guard_id]})})
        else:
            guard_sleep[guard_id].update(
                {timestamp: log_guard[timestamp][guard_id]}
            )

write_dict_to_file(guard_sleep, out_file_name)

guard_sleep_2 = {}
guard_state = "wake"
for guard_id in guard_list:
    #if guard_id == 2543:
    guard_id = str(guard_id)
    for timestamp in guard_sleep[guard_id]:
        if guard_id not in guard_sleep_2:
            guard_sleep_2.update(
                {
                    guard_id: collections.OrderedDict({})
                }
            )
        guard_sleep_2[guard_id].update(
            {
                timestamp: guard_sleep[guard_id][timestamp]
            }
        )

        if guard_sleep[guard_id][timestamp] == "asleep":
            guard_state = "asleep"
        elif guard_sleep[guard_id][timestamp] == "wake":
            #guard_state = "wake"
            continue
        elif guard_sleep[guard_id][timestamp] == "begin":
            continue
        next_timestamp = timestamp + 1
        counter = 0
        while next_timestamp not in guard_sleep[guard_id]:
            #print("{} - {} - {}".format(guard_id, next_timestamp,
            #    guard_sleep[guard_id][timestamp]))
            guard_sleep_2[guard_id].update(
                {next_timestamp: guard_state}
            )
            next_timestamp += 1
            if counter == 10:
                #print("sleep")
                #time.sleep(2)
                counter = 0
            else:
                counter +=1
        #next_state = guard_sleep[guard_id][timestamp + 1]

write_dict_to_file(guard_sleep_2, "1204_1_all_sleep")
