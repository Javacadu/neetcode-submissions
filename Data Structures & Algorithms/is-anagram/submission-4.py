class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            print(ord(s[i]) - ord('a'))
            letters[ord(t[i]) - ord('a')] -= 1
            print(ord(t[i]) - ord('a'))
        for i in letters:
            if i != 0:
                return False

        return True
