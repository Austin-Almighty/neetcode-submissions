# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            new_guess = (low + high) // 2
            result = guess(new_guess)
            if result == 0:
                return new_guess
            elif result == -1:
                high = new_guess - 1
            else:
                low = new_guess + 1

       
