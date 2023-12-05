class Solution:
    def numberOfMatches(self, n: int) -> int:
        counter=0
        while(n!=1):
          n,r=divmod(n,2)
          counter+=n
          n+=r
        return counter