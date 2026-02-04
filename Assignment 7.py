def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to track if a swap happened in this pass
        swapped = False

        # Last i elements are already in place, so we ignore them
        for j in range(0, n-i-1):

            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return arr

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(f"Sorted array: {sorted_list}")
