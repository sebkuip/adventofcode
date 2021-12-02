data = [l for l in open('input.txt', 'r').read().split('\n')]
depth = 0
forward = 0

for line in data:
    if line.startswith('down'):
        depth += int(line[-1])
    elif line.startswith('up'):
        depth -= int(line[-1])
    else:
        forward += int(line[-1])

print(depth)
print(forward)
print(depth * forward)