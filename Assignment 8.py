def quick_sort(arr):
    # Base case: lists with 0 or 1 element are already "sorted"
    if len(arr) <= 1:
        return arr

    # Selecting the middle element as the pivot
    pivot = arr[len(arr) // 2]

    # Divide: Create three sub-lists based on the pivot
    left = [x for x in arr if x < pivot]        # Elements amller than pivot
    middle = [x for x in arr if x == pivot]     # Elements equal to pivot
    right = [x for x in arr if x > pivot]       # Elements larger than pivot

    # Conquer and Combine: Recursively sort left and right, then join them
    return quick_sort(left) + middle +  quick_sort(right)

# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
print(f"Oringal: {my_list}")
print(f"Sorted: {quick_sort(my_list)}")
