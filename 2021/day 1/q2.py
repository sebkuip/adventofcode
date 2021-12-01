with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

counter = 0


for i in range(len(data)):
    if i == len(data) - 3:
        break
    if data[i] + data[i+1] + data[i+2] < data[i+1] + data[i+2] + data[i+3]:
        counter += 1

print(counter)