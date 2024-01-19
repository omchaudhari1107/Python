# Input: nums = [1,3,5,6], target = 5
# Output: 2

nums = [1,3,5,6]

def SearchInsertPosition(lst, target):
    for i in range(len(lst)):
        if lst[i] >= target:
            return i
    return len(lst)

print(SearchInsertPosition(nums, 5))  
print(SearchInsertPosition(nums, 2))  
print(SearchInsertPosition(nums, 7))  
