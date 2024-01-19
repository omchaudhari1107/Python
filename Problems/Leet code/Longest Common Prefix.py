class Solution(object):
    def Prefix(self, lst, i):
        if i<len(lst):
            string = lst[i]
            return string[0:2]

    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        for i in range(len(strs)):
            if i < len(strs):
                pre1 = self.Prefix(strs, i)
                if i<1:
                    pre2 = self.Prefix(strs, i)
                else:
                    pre2 = self.Prefix(strs, i+1)   
                print(pre1,pre2)
                if pre1 == pre2:
                    continue
                else:
                    return ""
        return self.Prefix(strs,0)

# Instantiate an object of the Solution class
solution = Solution()

# Call the longestCommonPrefix function on the object
strings = ["flower","flow","flight"]
pre=solution.longestCommonPrefix(strings)
print(pre)
