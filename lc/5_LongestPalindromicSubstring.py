class Solution(object):
    def longestPalindrome(self, s):
        longest=""
        if len(s)>0:
            longest=s[0]
        for i in range(len(s)):
            left=0
            right=0
            if i>=2 and s[i-2]==s[i]:
                left=i-3
                right=i+1
                while(right<len(s) and left>=0):
                    if s[left]==s[right]:
                        left-=1
                        right+=1
                    else:
                        break
                if len(longest)<right-left-1:
                    longest=s[left+1:right]
            if i>=1 and s[i-1]==s[i]:
                left=i-2
                right=i+1
                while(right<len(s) and left>=0):
                    if s[left]==s[right]:
                        left-=1
                        right+=1
                    else:
                        break
                if len(longest)<right-left-1:
                    longest=s[left+1:right]
            
        return longest
        """
        :type s: str
        :rtype: str
        """
        