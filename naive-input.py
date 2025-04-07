def naive_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found the target
    return -1  # Not found

# Take input from user
arr_input = input("Enter the elements of the rotated array (space-separated): ")
arr = list(map(int, arr_input.strip().split()))

target = int(input("Enter the number you want to search: "))

# Call the search function
result = naive_search(arr, target)

# Output
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
