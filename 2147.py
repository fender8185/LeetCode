class Solution:
    def numberOfWays(self, corridor: str) -> int:
      
        cs=corridor.count("S")
        if not cs or cs%2:
          return 0
        l=corridor.split("S")[2:-2:2]
        ans=1
        for i in l:
          ans*=(len(i)+1)
        return ans%(10**9+7)
