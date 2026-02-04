def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first and second halves
        merge_sort(L)
        merge_sort(R)

        i= j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i]. lower() < R[j].lower(): # .lower() ensures case-insensitive sorting
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage:
fruit_list = ["banana", "Apple", "cherry" ,"Date", "elderberry"]
print(f"Original: {fruit_list}")
sorted_fruit = merge_sort(fruit_list)
print(f"Sorted: {sorted_fruit}")