array = []

# take in a size of a int array
size = int(input("Enter the size of the array: "))

# loop through and take in numbers
for i in range(size):
    array.append(int(input("Enter a number: ")))

# sort the array
array.sort()

# print the sorted array
print("Sorted array: ", array)
