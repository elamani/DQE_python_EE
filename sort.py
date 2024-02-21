l1 = [6, 2, 5, 1, 4, 9]

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

# sorted list
print("Sorted List", l1)