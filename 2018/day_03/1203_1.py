# https://adventofcode.com/2018/day/3

def get_file(file_name):
    with open(file_name) as file:
        data = file.readlines()
    return data

def populate_2d_array(rows, cols):
    sheet = {}
    for i in range(0, rows):
        sheet[i] = {}
        for k in range(0, cols):
            sheet[i][k] = 0
    return sheet

#file_name = "1203_input_1.txt"
file_name = "1203_input.txt"
data = get_file(file_name)
sheet = populate_2d_array(1000, 1000)
for line in data:
    line_split = line.split()
    pos = line_split[2].split(",")
    col_beg = pos[0]
    row_beg = pos[1].replace(':','')

    dim = line_split[3].split('x')
    col_end = int(col_beg) + int(dim[0])
    row_end = int(row_beg) + int(dim[1])

    for k in range(int(col_beg), int(col_end)):
        for i in range(int(row_beg), int(row_end)):
            sheet[k][i] += 1

#over_2_count = 0
#for i in range(0, 1000):
#    for k in range(0, 1000):
#        if sheet[i][k] >= 2:
#            over_2_count += 1
#print(over_2_count)

for line in data:
    line_all_ones = True
    line_split = line.split()
    pos = line_split[2].split(",")
    col_beg = pos[0]
    row_beg = pos[1].replace(':','')

    dim = line_split[3].split('x')
    col_end = int(col_beg) + int(dim[0])
    row_end = int(row_beg) + int(dim[1])

    for k in range(int(col_beg), int(col_end)):
        for i in range(int(row_beg), int(row_end)):
            if sheet[k][i] > 1:
                line_all_ones = False
    if line_all_ones == True:
        print(line_split[0])
