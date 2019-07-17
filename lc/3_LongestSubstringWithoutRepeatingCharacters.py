class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if(s==""):
            return 0
        longest=1
        candidate=[]
        for num in range(len(s)):
            #print(candidate,s[num])
            next_candidate=[]
            for num_can in range(len(candidate)):
                if (s[num] in candidate[num_can])==False:
                    next_candidate.append(candidate[num_can]+s[num])
                    
                    if len(candidate[num_can]+s[num])>longest:
                        longest=len(candidate[num_can]+s[num])
            next_candidate.append(s[num])
            candidate=next_candidate
        return longest
           
        """
        :type s: str
        :rtype: int
        """
        