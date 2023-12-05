class Solution:
    def reverse(self, x: int) -> int:
      neg=False
      if x<0:
        neg=True
        x=-x
      s=str(x)[::-1]
      new_x=int(s)
      if neg:
        new_x=-new_x
      if -2**31<=new_x<=2**31-1:
        return new_x
      else:
        return 0


