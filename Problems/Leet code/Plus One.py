# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

digit = [9]

def plusOne(lst):
    digits_str = ''.join(map(str, lst))
    number = int(digits_str)
    number+=1
    number_str = str(number)
    lst = [int(i) for i in number_str]
    print(lst)

plusOne(digit)
