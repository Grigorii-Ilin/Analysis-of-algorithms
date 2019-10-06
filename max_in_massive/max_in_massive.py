import random

ITERATIONS = 10000
MAS_LEN = 1000

counts_holder = []

for iter in range(ITERATIONS):   
    mas = [random.random() for i in range(MAS_LEN)]
    operations_count = 0
    max_num = mas[0]

    for i in range(1, MAS_LEN):
        if max_num < mas[i]:
            max_num = mas[i]
            operations_count+=1

    counts_holder.append(operations_count)
    
counts_mean = sum(counts_holder) / len(counts_holder)
print(counts_mean)

