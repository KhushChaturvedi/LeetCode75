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
