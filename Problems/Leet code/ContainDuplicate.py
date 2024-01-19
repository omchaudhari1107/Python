# Input: nums = [1,2,3,1]
# Output: true
nums=[2,1,4]

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()#set is faster in terms of searching
        for num in nums:
            if num in num_set:
                print(num)
            num_set.add(num)   
        
# Create an instance of the Solution class
solution = Solution()

solution.containsDuplicate(nums)
