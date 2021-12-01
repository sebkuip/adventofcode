with open('input.txt', 'r') as f:
    data = f.readlines()

    for i, line in enumerate(data):
        data[i] = int(line)

counter = 0

for i in range(len(data)):
    if i == len(data) - 3:
        break
    if data[i] + data[i+1] + data[i+2] < data[i+1] + data[i+2] + data[i+3]:
        counter += 1

print(counter)