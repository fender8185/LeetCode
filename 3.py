class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      ans=0
      i=0
      for j,c in enumerate(s):
        if c in s[i:j]:
          while(s[i]!=c):
            i+=1
          i+=1
        ans=max(ans,j-i+1)
      return ans