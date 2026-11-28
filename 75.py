# Problem 1: merge strings alternately

word1 = "abc"
word2 = "pqr"


class Solution:
    def mergeAlternately(self, word1, word2):

        result = ""

        for a, b in zip(word1, word2):
            result += a + b

        result += word1[len(word2) :] + word2[len(word1) :]
        return result


# Problem 2: Greates common divisor of strings

str1 = "ABABAB"
str2 = "AB"


class Solution:
    def greatestCommonDivisor(self, str1, str2):

        shortest = min(len(str1), len(str2))

        for i in range(shortest, 0, -1):
            guess = str1[:i]

            if len(str1) % i == 0 and len(str2) % i == 0:
                if (
                    guess * (len(str1) // i) == str1
                    and guess * (len(str2) // i) == str2
                ):
                    return guess

        return ""


# Problem 3: kids with greates number of candies

candies = [2, 3, 5, 1, 3]
extracandies = 3


class Solution:
    def kidsWithCandies(self, candies, extracandies):

        greatest = max(candies)
        answers = []

        for c in candies:
            total = c + extracandies

            if total >= greatest:
                answers.append(True)
            else:
                answers.append(False)

        return answers


# Problem 4: Can Place Flowers

flowerbed = [1, 0, 0, 0, 1]
n = 1


class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        count = 0

        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                count += 1

        if count >= n:
            return True
        else:
            return False


# Problem 5: reverse vowels of a string

s = "IceCreAm"


class Solution:
    def reverseVowels(self, s):

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        letters = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if letters[left] not in vowels:
                left += 1
            elif letters[right] not in vowels:
                right -= 1
            else:
                letters[left], letters[sright] = letters[right], letters[left]
                left += 1
                right -= 1

        return "".join(letters)


# Problem 6: Reverse words in string

s = "the sky is blue"


class Solution:
    def reverseWords(self, s):

        words = s.split()
        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)


# Problem 7: Product of array except self

nums = [1, 2, 3, 4]


class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        left = [1] * n
        right = [1] * n
        running = 1
        rightRunning = 1
        answer = []

        for i in range(len(nums)):
            left[i] = running
            running = running * nums[i]

        for i in range(n - 1, -1, -1):
            right[i] = rightRunning
            rightRunning = rightRunning * nums[i]

        for i in range(n):
            answer.append(left[i] * right[i])

        return answer


# Problem 8: increasing triplet subsequence

nums = [1, 2, 3, 4, 5]

first = float("inf")
second = float("inf")

for x in nums:
    if x <= first:
        first = x
    elif x <= second:
        second = x
    else:
        return True

return False


# Problem 9: String Compression

chars = ["a", "a", "b", "b", "c", "c", "c"]


class Solution:
    def compress(self, chars):

        write = 0
        count = 0

        for read in range(len(chars)):
            count += 1

            if read + 1 == len(chars) or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1

                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                count = 0

        return write


# Problem 10: Move zeroes

nums = [0, 1, 0, 3, 12]


class Solution:
    def moveZeroes(self, nums):

        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# Problem 11: In subsequence

s = "abc"
t = "ahbgdc"


class Solution:
    def inSubsequence(self, s, t):

        i = 0

        for ch in range(len(t)):
            if i < len(s) and t[ch] == s[i]:
                i += 1

        return i == len(s)


# Problem 12: Container with the most water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h

            if area > best:
                best = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best


# Problem 13: Max numbers of k sum pairs

nums = [1, 2, 3, 4]
k = 5


class Solution:
    def maxOperations(self, max, k):

        nums.sort()
        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            if nums[left] + nums[right] == k:
                ops += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return ops


# Problem 14: Maximum Average Subarray I

nums = [1, 12, -5, -6, 50, 3]
k = 4


class Solution:
    def findMaxAverage(self, nums, k):

        window = sum(nums[:k])
        best = window

        for i in range(k, len(nums)):
            window = nums[i] + window - nums[i - k]

            if window > best:
                best = window

        average = best / k

        return average


# Problem 15: Maximum number of vowels in a substring of given length

s = "abciiidef"
k = 3


class Solution:
    def maxVowels(self, s, k):
        count = 0
        vowels = ("a", "e", "i", "o", "u")

        for letter in s[:k]:
            if letter in vowels:
                count += 1

        best = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1

            if count > best:
                best = count

        return best


# Problem 16: Max concecutives ones III

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


class Solution:
    def longestOnes(self, nums, k):

        left = 0
        best = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


# Problem 17: Longest Subarray of 1's After Deleting One Element

nums = [1, 1, 0, 1]


class Solution:
    def longestSubarray(self, nums):

        left = 0
        zeros = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best - 1


# problem 18: Find the Highest Altitude

gain = [-5, 1, 5, 0, -7]


class Solution:
    def largestAltitude(self, gain):

        alt = 0
        best = 0

        for i in range(len(gain)):
            alt += gain[i]

            if alt > best:
                best = alt

        return best


# Problem 19: Find pivot index

nums = [1, 7, 3, 6, 5, 6]


class Solution:
    def pivotIndex(self, nums):

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1


# Problem 20: Find the Difference of Two Arrays

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]


class Solution:
    def findDifference(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)

        first = []
        second = []

        for number in set1:
            if number not in set2:
                first.append(number)

        for number in set2:
            if number not in set1:
                second.append(number)

        return [first, second]


# Problem 21: Unique number of occurences

arr = [1, 2, 2, 1, 1, 3]


class Solution:
    def uniqueOccurrences(self, arr):

        array = sorted(arr)
        counts = []

        i = 0
        while i < len(array):
            j = i

            while j < len(array) and array[j] == array[i]:
                j += 1

            counts.append(j - i)

            i = j

            return len(set(counts) == len(counts))


# Problem 22: Determine if Two Strings Are Close

word1 = "abc"
word2 = "bca"


class Solution:
    def closeStrings(self, word1, word2):

        if len(word1) != len(word2):
            return False

        count1 = {}

        for letters in word1:
            if letters in count1:
                count1[letters] += 1
            else:
                count1[letters] = 1

        count2 = {}

        for letters in word2:
            if letters in count2:
                count2[letters] += 1
            else:
                count2[letters] = 1

        if set(count1) != set(count2):
            return False

        return sorted(count1.values()) == sorted(count2.values())


# Problem 23: Equal row and column pairs

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]


class Solution:
    def equalPairs(self, grid):

        count = 0
        size = len(grid)

        for r in range(size):
            row = grid[r]

            for c in range(size):
                column = []

                for k in range(size):
                    number = grid[k][c]
                    column.append(number)

                if row == column:
                    count += 1

        return count


# Problem 24: Removing Stars From a String

s = "leet**cod*e"


class Solution:
    def removeStars(self, s):

        stack = []

        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


# Problem 25: Asteroid Collision

asteroids = [5, 10, -5]


class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for a in asteroids:
            alive = True

            while alive is True and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive is True:
                stack.append(a)

        return stack


# Problem 26: Decode String

s = "3[a]2[bc]"


class Solution:
    def decodeString(self, s):

        current = ""
        number = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == "[":
                stack.append((current, number))
                current = ""
                number = 0

            elif ch == "]":
                previous, times = stack.pop()
                current = previous + current * times

            else:
                current += ch

        return current


# Problem 27:  Number of Recent Calls

from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = dequeue()

    def ping(self, t):
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
