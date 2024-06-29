# create function to sort an array methods bubble
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                


# create function to sort an array methods select
def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element of the unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]      




# create test for selection_sort
test = [21, 12, 13, 1, 2, 3, 45, 5, 6]
selection_sort(test)
print(test)  # [1, 2, 3, 5, 6, 12, 13, 21, 45]

# create pytest for function def selection_sort


