data = []
with open('tests.txt', 'r') as file:
    for i in file:
        data.append(i)
not_none = []
end_vals = {}
for i in data:
    i.strip()
    # print(i)
    string = i.split(',')
    # print(string[2])
    if 'NONE' not in string[-1]:

        if float(string[-1]) <= 3.5:
            not_none.append(i)
count = 0
for i in not_none:
    if i not in end_vals.values():
        end_vals[count] = i
        count += 1
print(end_vals)
count = 0
for i in end_vals:
    with open('end.txt', 'a') as file:
        file.write('{}'.format(end_vals[i]))
    count += 1
