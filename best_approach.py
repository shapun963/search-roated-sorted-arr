def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# 🔽 Default input values
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# 🧪 Test the function
result = search(nums, target)

# 📤 Print the result
print(f"Index of target {target} in array {nums} is: {result}")

