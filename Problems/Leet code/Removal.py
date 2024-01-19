# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation:
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number possible.
nums = [0,-4,19,1,8,-2,-3,5]


def Removal(arr):
    count_positive = 0
    count_negative = 0
    temp = arr
    temp = sorted(temp)
    Min = temp[0]
    Max = temp[len(arr) - 1]
    if Min == Max:
        return 1
    if Max or Min in arr:
        index_Max = arr.index(Max)
        index_Min = arr.index(Min)
        print(index_Max,index_Min)
    for i in arr:
        index_i = arr.index(i)
        if index_i<=index_Max:
            count_positive+=1
        if index_i>=index_Min:
            count_negative+=1
    print(count_positive,count_negative)
    return count_positive+count_negative
removed = Removal(nums)
print(removed)
