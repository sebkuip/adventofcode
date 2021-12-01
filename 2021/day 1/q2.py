with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

counter = 0


for i in range(len(data)):
    # break at the end of the dataset
    if i == len(data) - 3:
        break
    # check if the next numberset is larger than the current numberset
    if data[i] + data[i+1] + data[i+2] < data[i+1] + data[i+2] + data[i+3]:
        counter += 1

print(counter)