class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        #v1
        dic[0]=[4,6]
        dic[1]=[6,8]
        dic[2]=[7,9]
        dic[3]=[4,8]
        dic[4]=[0,3,9]
        dic[6]=[0,1,7]
        dic[7]=[2,6]
        dic[8]=[1,3]
        dic[9]=[2,4]
        '''

        '''
        #v2
        dic[0]=[4,4]
        dic[1]=[4,8]
        dic[2]=[7,7]
        #dic[3]=[4,8]
        dic[4]=[0,1,7]
        #dic[6]=[0,1,7]
        dic[7]=[2,4]
        dic[8]=[1,1]
        #dic[9]=[2,4]
        '''
        """
        for v in l:
          c=[0]*9
          c[v]=1
          for _ in range(n-1):
            temp=[0]*9
            for j in l:
              for k in dic[j]:
                if j not in l2:
                  temp[k]+=2*c[j]
                else:
                  temp[k]+=c[j]
            #print(temp)
            c=temp
          if v in l2:
            ans+=(2*sum(c))%(10**9+7)
          else:
            ans+=sum(c)%(10**9+7)
        return ans%(10**9+7)

        """
        '''
        #v3
        dic[0]=[4]
        dic[1]=[4,8]
        dic[2]=[7]
        dic[4]=[0,1,7]
        dic[7]=[2,4]
        dic[8]=[1]
        '''



        '''
        #v4
        ans=0

        @cache
        def f(v,round):
          if round==2:
            if v==4:
              return 3
            else:
              return 2
          else:
            if v==0:
              return f(4,round-1)*2
            elif v==1:
              return f(4,round-1)+f(8,round-1)
            elif v==2:
              return f(7,round-1)*2
            elif v==4:
              return f(0,round-1)+f(1,round-1)+f(7,round-1)
            elif v==7:
              return f(2,round-1)+f(4,round-1)
            else:
              return f(1,round-1)*2
        ans=0
        for i in [1,4,7,2,8,0]:
          if i in {1,4,7}:
            ans+=f(i,n)*2
          else:
            ans+=f(i,n)
          ans%=(10**9+7)
        return ans%(10**9+7)

        '''

        
        
        #v5
        #  0 1 2 4 7 8
        #  0 1 2 3 4 5
        '''
        MOD=(10**9+7)
        l=[1,2,1,2,2,1]
        for _ in range(n-1):
          t0=l[3]
          t1=l[3]+l[5]*2
          t2=l[4]
          t4=l[0]*2+l[1]+l[4]
          t7=l[2]*2+l[3]
          t8=l[1]
          l=[t0%MOD,t1%MOD,t2%MOD,t4%MOD,t7%MOD,t8%MOD]
                      
          #l=[l[3],(l[3]+l[5]*2),l[4],(l[0]*2+l[1]+l[4]),l[2]*2+l[3],l[1]]
        return sum(l)%MOD if n!=1 else 10
        '''

        #v6
        '''
        after print the l each round we will find we have the other pair 
        (2,8) and 7 can also be replaced by operator
        '''        
        
        #v6
        '''
        time 99% space 99%
        '''
        MOD=(10**9+7)
        n-=1
        #  0 1 2 3 
        #  0 1 2 4
        l=[1,2,1,2]
        for _ in range(n):
          t0=l[3]
          t1=l[3]+l[2]*2
          t2=l[1]
          t4=(l[0]+l[1])*2
          l=[t0%MOD,t1%MOD,t2%MOD,t4%MOD]
        return (sum(l)+sum(l[1:3]))%MOD if n else 10