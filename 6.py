class Solution:
    def convert(self, s: str, numRows: int) -> str:
      '''
      n (n-2) n
      '''
      if numRows<2:
        return s
      l=list()
      cyc=numRows*2-2
      while(len(s)>=cyc):
        Q=deque(s[:cyc])
        l.append(Q)
        s=s[cyc:]
      
      if s:
        s+=(cyc-len(s))*" "
        Q=deque(s)
        l.append(Q)
      ans=""
      for i in range(len(l)):
        ans+=l[i].popleft()

      for j in range(numRows-2):
        for i in range(len(l)):

            ans+=l[i].popleft()
            ans+=l[i].pop()
      for i in range(len(l)):
        ans+=l[i].popleft()
      return ans.replace(" ","")
        
