class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        將題目拆解成找到第K(中位數)個數
        """
        def f(a,b,k):
          #只有一個array了就表示第k個數即為所求
          if not a:
            return b[k]
          if not b:
            return a[k]
          #取中位數的index 和 value
          idxa,idxb=len(a)//2,len(b)//2
          ma,mb=a[idxa],b[idxb]
          #如果兩個list的左側數目小於k，我們將中位數較小的左側(含)刪除
          if idxa+idxb<k: 
            if ma<mb:
              return f(a[idxa+1:],b,k-idxa-1)
            else:
              return f(a,b[idxb+1:],k-idxb-1)
          #反之 則刪除右側
          else:
            if ma>mb:
              return f(a[:idxa],b,k)
            else:
              return f(a,b[:idxb],k)


        totall=len(nums1)+len(nums2)
        if totall%2:
          return f(nums1,nums2,totall//2)
        #偶數解則取兩數平均
        else:
          return (f(nums1,nums2,totall//2)+f(nums1,nums2,totall//2-1))/2.0
        