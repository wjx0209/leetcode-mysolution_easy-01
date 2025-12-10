class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 +num2
# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return[kelvin, fahrenheit]
# https://leetcode.com/problems/convert-the-temperature/description/
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n < 2:
            return(2)
        else:
            if n % 2 == 0:
                return(n)
            else:
                return(2 * n)
# https://leetcode.com/problems/smallest-even-multiple/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left.val + root.right.val ==root.val:
            return(True)
        else:
            return(False)
# https://leetcode.com/problems/root-equals-sum-of-children/description/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return(ans) 
# https://leetcode.com/problems/xor-operation-in-an-array/description/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        #可以定义n = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
# https://leetcode.com/problems/number-of-good-pairs/description/
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0 
        n = len(arr)
        for i in range(n):
            for j in range(i+1,  n):
                for k in range(j+1, n):
                    if 0 <= i < j < k < len(arr) and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
# https://leetcode.cn/problems/count-good-triplets/?envType=study-plan-v2&envId=primers-list
class Solution:
    def toLowerCase(self, s: str) -> str: 
        result = []
        for char in s:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return "".join(result)
# https://leetcode.com/problems/to-lower-case/description/
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num
# https://leetcode.com/problems/add-digits/description/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        if n == 0:
            return 0 
        temp = n
        while temp > 0:
            digit = temp % 10
            product *= digit
            sum += digit
            temp = temp // 10
        
        return product - sum
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
# https://leetcode.com/problems/power-of-two/description/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
# https://leetcode.com/problems/power-of-three/description/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        
        return n == 1
# https://leetcode.com/problems/ugly-number/description/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result= []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
# https://leetcode.com/problems/shuffle-the-array/description/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
# https://leetcode.com/problems/transpose-matrix/description/
# another solution:
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        trans = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                trans[j][i] = matrix[i][j]
        return trans
# https://leetcode.com/problems/transpose-matrix/description/
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_score = 0
        for i in range(1, n):
            left = s[: i]
            right = s[i: ]
            zero = left.count('0')
            one = right.count('1')
            score = zero + one
            max_score = max(max_score, score)
        return max_score
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word and word[0] in vowel and word[-1] in vowel:
                count += 1
        return count
# https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
                 

        



        
            
        
