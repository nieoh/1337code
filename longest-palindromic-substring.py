class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        cand = ''
        for idx, char in enumerate(s):
            cand = char
            print('middle', cand, idx)
            left = idx - 1
            right = idx + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    cand = s[left] + cand + s[right]
                    left -= 1
                    right += 1
                else:
                    left = -1
            if len(cand) > len(ret):
                ret = cand
            if idx!= len(s)-1 and s[idx] == s[idx+1]:
                cand = char + char
                left = idx -1
                right = idx + 2
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        cand = s[left] + cand + s[right]
                        left -= 1
                        right += 1
                    else:
                        left = -1
                if len(cand) > len(ret):
                    ret = cand
                    
        return ret
