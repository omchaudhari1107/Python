class Solution(object):
    def merge(self, lst1,m, lst2,n):
        # for i in range(len(lst1)):
        #     lst1[i]=lst1[i]
        lst = lst1[0:m]+lst2[0:n]
        lst = sorted(lst)
        return lst
# Create an instance of the Solution class
solution = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(solution.merge(nums1,3, nums2,3))