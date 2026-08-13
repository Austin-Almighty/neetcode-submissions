class Solution:
    def isPalindrome(self, s: str):
        s_stripped = s.lower()
        s_cleaned = "".join([alnum for alnum in s_stripped if alnum.isalnum()])

        head = 0
        tail = len(s_cleaned) - 1

        while head <= tail:
            if s_cleaned[head] != s_cleaned[tail]:
                return False
            head += 1
            tail -= 1

        return True

