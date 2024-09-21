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

#this idea is also using dfs but not in a recursive way (offical solution), but the result saying this method runs far more fast than the first one(with far fewer space)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans

#this idea is using python's inbuilt function sorted, but the time complexity is O(nlogn)

    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(i) for i in range(1,n+1)]
        ans.sort()
        return [int(i) for i in ans]