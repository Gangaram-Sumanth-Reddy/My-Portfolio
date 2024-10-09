def count_swaps(arr):
    n = len(arr)
    swap_count = 0
    # Create a copy of the array for sorting
    temp_arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:  # Ascending order
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
                swap_count += 1
    return swap_count

def count_swaps_desc(arr):
    n = len(arr)
    swap_count = 0
    # Create a copy of the array for sorting
    temp_arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] < temp_arr[j + 1]:  # Descending order
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
                swap_count += 1
    return swap_count

def minimum_swaps_to_make_beautiful(n, arr):
    # Calculate swaps for ascending order
    asc_swaps = count_swaps(arr)
    
    # Calculate swaps for descending order
    desc_swaps = count_swaps_desc(arr)

    # Return the minimum of the two
    return min(asc_swaps, desc_swaps)

# Input
N = int(input())
Arr = list(map(int, input().split()))

# Output
print(minimum_swaps_to_make_beautiful(N, Arr))