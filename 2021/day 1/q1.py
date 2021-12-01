with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

counter = 0

for i in range(len(data)):
    # break at the end of the dataset
    if i == len(data) - 1:
        break
    # check if the next number is larger than the current number
    if data[i] < data[i + 1]:
        counter += 1

print(counter)