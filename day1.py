with open('input1.txt', 'r') as f:
    text_input = f.read()

left_list = []
right_list = []

for line in text_input.split('\n'):
    split_line = line.split('   ')
    left_list.append(split_line[0])
    right_list.append(split_line[1])

left_list = sorted(left_list)
right_list = sorted(right_list)

# part 1
distances = [abs(int(a)-int(b)) for a,b in zip(left_list, right_list)]
print(sum(distances))

# part 2
left_dict = {n:0 for n in left_list}
for n in right_list:
    if n in left_dict:
        left_dict[n] += int(n)
print(sum(left_dict.values()))