with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

counter = sum(data[i] < data[i + 1] for i in range(len(data) - 1))

print(counter)