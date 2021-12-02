data = [int(line.strip()) for line in open('input.txt', 'r')]
print(sum(data[i] < data[i+1] for i in range(len(data) - 1)))