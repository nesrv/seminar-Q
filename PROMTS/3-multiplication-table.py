# make a multiplication table using two cycles

size = int(input("Enter the size of the multiplication table: "))

# Print the header row
print("  |", end="")
for i in range(1, size + 1):
    print(f"{i:3}", end=" ")
print()
print("-" * (size * 4 + 3))

# Print the multiplication table
for i in range(1, size + 1):
    print(f"{i:2}|", end="")
    for j in range(1, size + 1):
        print(f"{i * j:3}", end=" ")
    print()


d = {1: 2, 2: 3, 3: 4}
print(d)
d[4] = 5
print(d)
del d[4]
