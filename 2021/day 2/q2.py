data = [l for l in open('input.txt', 'r').read().split('\n')]
depth = 0
forward = 0
aim = 0

for line in data:
    if line.startswith('down'):
        aim += int(line[-1])
    elif line.startswith('up'):
        aim -= int(line[-1])
    else:
        forward += int(line[-1])
        depth += int(line[-1])*aim

print(depth)
print(forward)
print(depth*forward)