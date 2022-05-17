class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Using list comprehension to reverse letters to store in list and compare to original number
        s = str(x)
        return s==s[::-1]
