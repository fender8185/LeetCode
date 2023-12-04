class Solution:
    def largestGoodInteger(self, num: str) -> str:
      pre=None
      c=0
      ans=-1
      s,e=0,len(num)-3
      while(s<=e):
        if num[s]==num[s+1]:
          if num[s]==num[s+2]:
            ans=max(ans,int(num[s]))
            s+=3
          else:
            s+=2
        else:
          s+=1
      return str(ans)*3 if ans!=-1 else ""
