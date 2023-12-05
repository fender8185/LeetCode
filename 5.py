class Solution:
    def longestPalindrome(self, s: str) -> str:
      '''
      this is a way like BFS so it's not very effective,but this BFS-like solution
      can get nice performance on short palindromic.
      
      this is a good problem to show us the bottom-up is not 100% faster
      than top-down
      
      maybe we should check the most opportunity index (middle of the s)
      if we found it can expand then we could remove some candidate from head and end
      '''

      if len(s)<2:
        return s
      ans=[]
      for i in range(len(s)-1):
        ans.append((i,i))
      for i in range(len(s)-1):
        if s[i]==s[i+1]:
          ans.append((i,i+1))

      while(1):
        temp=[]
        for i,j in ans:
          if i>0 and j<len(s)-1 and s[i-1]==s[j+1]:
            temp.append((i-1,j+1))
        if not temp:
          break
        ans=temp
      return s[ans[-1][0]:ans[-1][1]+1]
 
