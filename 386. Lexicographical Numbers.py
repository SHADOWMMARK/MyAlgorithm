# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

# the idea is easy using the dfs!

def lexicalOrder(self, n: int) -> List[int]:
    ans = []
    def dfs(num):
          if num>n:
              return
          ans.append(num)
          for nex in range(num*10,num*10+10):
              dfs(nex)
    for num in range(1,10):
        dfs(num)
    return ans  
