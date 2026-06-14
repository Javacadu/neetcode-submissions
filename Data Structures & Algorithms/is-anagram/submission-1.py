class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26

        for i in range(len(s)):
            letters[ord('a') - ord(s[i])] += 1
            print(ord('a') - ord(s[i]))
            letters[ord('a') - ord(t[i])] -= 1
            print(ord('a') - ord(t[i]))
        for i in letters:
            if i != 0:
                return False

        return True
