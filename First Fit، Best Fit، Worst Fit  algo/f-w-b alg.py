# First Fit Algorithm
def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation

# Best Fit Algorithm
def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]
    return allocation

# Worst Fit Algorithm
def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= processes[i]
    return allocation

blocks = [20, 10, 30]
processes = [15, 10, 25]

print("First Fit Allocation:", first_fit(blocks.copy(), processes))
print("Best Fit Allocation:", best_fit(blocks.copy(), processes))
print("Worst Fit Allocation:", worst_fit(blocks.copy(), processes))

