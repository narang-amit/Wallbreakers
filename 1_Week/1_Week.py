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

def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        lstVow = []
        for i in s:
            if i in vowels: 
                lstVow.append(i)
        lstVow = lstVow[::-1]
        cnt = 0
        holder = ""
        for i in range(len(s)): 
            if s[i] in vowels: 
                holder += lstVow[cnt]
                cnt += 1
            else:
                holder += s[i]
        return holder

# Question #13

def fizzBuzz(self, n: int) -> List[str]:
        holder = list()
        for i in range(1,n+1):
            if i % 15 == 0:
                holder.append("FizzBuzz")
            elif i % 3 == 0:
                holder.append("Fizz")
            elif i % 5 == 0:
                holder.append("Buzz")
            else:
                holder.append(str(i))
        return holder

# Question #14

def hammingDistance(self, x: int, y: int) -> int:
        x = "{0:b}".format(x)
        y = "{0:b}".format(y)
        if len(x) < len(y):
            x = x.zfill(len(y))
        elif len(x) > len(y):
            y = y.zfill(len(x))
        return sum(1 for a, b in zip(x, y) if a != b)

# Question #15

def findComplement(self, num: int) -> int:
        
        def getBit(num):
            holder = []
            while num != 0:
                if num % 2 == 0:
                    holder.append(0)
                else:
                    holder.append(1)
                num //= 2
            return holder[::-1]
        
        bit = getBit(num)
        
        a = [1 if x == 0 else 0 for x in bit]

        tempSum = 0
        curr = 1
        for i in a[::-1]:
            tempSum += i * curr
            curr *= 2
        return tempSum

# Question #16

def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())

# Question #17

# Question #18
def reverseWords(self, s: str) -> str:
        tmp = s.split()
        a = [x[::-1] for x in tmp]
        return " ".join(a)

# Question #19
def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        holder = []
        for i in range(left,right+1):
            j = list(str(i))
            if "0" not in j and all([i % int(k) == 0 for k in j]):
                holder.append(i)
        return holder

# Question #20

def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        a = [x[::-1] for x in A]
        b = [[1 if x == 0 else 0 for x in g] for g in a]
        return b

# Question #21

def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Question #22

def binaryGap(self, N: int) -> int:
        x = "{0:b}".format(N).strip("0")
        
        print(x)
        if x.count("1") < 2:
            return 0 
        else: 
            ind = 0
            currMax = 0
            temp = 0
            while ind < len(x):
                if x[ind] == "1":
                    temp = 1
                    ind += 1
                    while ind < len(x) and x[ind] != "1":
                        temp += 1
                        ind += 1
                    currMax = max(temp,currMax)
                else:
                    ind += 1
            return currMax

# Question #23
def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]