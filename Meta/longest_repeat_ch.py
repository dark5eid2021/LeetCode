"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same
 letter you can get after performing the above operations.


"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - 1 + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - 1 + 1)
        
        return res