data = [int(line.strip()) for line in open('input.txt', 'r')]
print(sum(data[i] < data[i+3] for i in range(len(data) - 3)))
