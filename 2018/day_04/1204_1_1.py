import json

def get_json_file(in_file_name):
    with open(in_file_name) as json_data:
        data = json.load(json_data)
    return data

def get_list_from_file(in_file_name):
    out_data = []
    with open(in_file_name) as in_data:
        data = in_data.readlines()
        for i in data:
            out_data.append(int(i))
    return out_data

def get_sleep_count(guard_id, log):
    sleep_count = 0
    for timestamp in log[guard_id]:
        if log[guard_id][timestamp] == "asleep":
            sleep_count += 1
    return sleep_count

def get_min_asleep(guard_id, log):
    asleep_min = [0] * 60
    for timestamp in log[guard_id]:
        minute = int(timestamp[-4:])
        if log[guard_id][timestamp] == "asleep":
            #if minute == 15:
            #    print("{} - {} - {} - {}".format(
            #        guard_id, timestamp, minute, asleep_min[minute])
            #    )
            asleep_min[minute] += 1
    return asleep_min

def print_list(in_list):
    i = 0
    for minute_count in in_list:
        print("{}: {}".format(i, minute_count))
        i += 1

def get_minute_asleep_most(in_list):
    for minute in range(0, 60):
        if in_list[minute] == max(in_list):
            print("minute: {} count: {}".format(
                minute, in_list[minute]))

guard_list = get_list_from_file("1204_guard_list")
guard_log = get_json_file("1204_1_all_sleep")

#for guard_id in guard_list:
#    min_asleep = get_sleep_count(str(guard_id), guard_log)
#    print("{}: {}".format(guard_id, min_asleep))

most_sleepy_guard = 1571
most_sleepy_minute = 54

asleep_min = get_min_asleep(str(most_sleepy_guard), guard_log)
#print_list(asleep_min)
#print(max(asleep_min))
get_minute_asleep_most(asleep_min)

for guard_id in guard_list:
    asleep_min = get_min_asleep(str(guard_id), guard_log)
    print("guard_id :{} ".format(guard_id), end="")
    get_minute_asleep_most(asleep_min)


