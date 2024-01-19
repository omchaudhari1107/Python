class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        underscore = []
        unique_nums = set(nums)
        unique_nums = list(unique_nums)
        # for i in range(original_len - len(unique_nums)):
        #     underscore.append(0)
        ans = unique_nums + underscore
        # ans = list(ans)
        # print(type(ans))
        return ans


solution = Solution()
nums = [1, 1, 2, 2, 4, 1, 6, 2, 7, 2, 5, 1, 6, 5, 2, 5, 1]
data = solution.removeDuplicates(nums)
print(data)
