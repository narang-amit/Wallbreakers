from collections import Counter

# Question #1

def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = dict()
        pos = 0
        while pos < len(nums): 
            if (target-nums[pos] not in diction):
                diction[nums[pos]] = pos
                pos += 1
            else:
                return [diction[target-nums[pos]],pos]

# Question #2

def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            small = min(strs,key=len)
            for i in range(len(small)):
                if not all([x[i] == small[i] for x in strs]):
                    return small[:i]
            return small
        return ""

# Question #3

def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        if digits[len(digits)-1] >= 10:
            tmpInd = len(digits) - 1
            while digits[tmpInd] >= 10 and tmpInd != 0:
                digits[tmpInd] -= 10
                tmpInd -= 1
                digits[tmpInd] += 1
            if tmpInd == 0 and digits[tmpInd] >= 10:
                digits[tmpInd] -= 10
                return [1] + digits
        return digits

# Question #4

def isPalindrome(self, s: str) -> bool:
        stripped = [x for x in s.lower() if x.isalnum()]
        return stripped == stripped[::-1]

# Question #5

# Question #6

def singleNumber(self, nums: List[int]) -> int:
        standard = 0
        for num in nums:
            standard = num ^ standard
        
        return standard

# Question #7

def titleToNumber(self, s: str) -> int:
        strin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        holder = 0
        tmp = s[::-1]
        curr = 1
        for i in tmp:
            holder += curr * (strin.index(i) + 1)
            curr *= 26
        return holder

# Question #8

# Question #9

def isPowerOfTwo(self, n: int) -> bool:
        a = 1
        while a < n: 
            a *= 2
        return a == n

# Question #10

def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2

# Question #11

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] = s[len(s)-1-i],s[i]

# Question #12



