with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

counter = sum(data[i] + data[i+1] + data[i+2] < data[i+1] + data[i+2] + data[i+3] for i in range(len(data) - 3))

print(counter)