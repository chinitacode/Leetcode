
'''
416. Partition Equal Subset Sum [Medium]

问题可以看做一个背包大小为Sum//2的0-1背包问题。

dp[i][j]表示用前i个num可以凑齐j的组合方式个数：
dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i]]

可以优化空间复杂度为一维数列（逆序）：
dp[j] = dp[j] + dp[j-nums[i]]

使dp[0] = 1,即刚好当前num就可以凑齐j的组合个数为1；
最后返回True如果dp[Sum//2]不为0，且为2的倍数，也就是说有2的整数倍种方式凑齐Sum//2。

Time: O(N + N*Sum//2) = O(N*Sum//2), N为nums的元素个数，Sum为nums的元素之和。
Space: O(Sum//2)
Runtime: 1040 ms, faster than 35.83% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.1 MB, less than 13.64% of Python3 online submissions for Partition Equal Subset Sum.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2: return False
        cap = Sum // 2
        dp = [0] * (cap + 1)
        dp[0] = 1
        for num in nums:
            for j in range(cap, num -1, -1):
                dp[j] = dp[j] + dp[j-num]
        return True if (dp[cap] != 0 and dp[cap]%2 == 0) else False


'''
494. Target Sum [Medium]
[Method 1]: DP
该问题可以转换为 416.Partition Equal Subset Sum 问题，从而使用 0-1 背包的方法来求解。
可以将这组数看成两部分，P 和 N，其中 P 使用正号，N 使用负号，有以下推导：
                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
因此只要找到一个子集，令它们都取正号，并且和等于 (target + sum(nums))//2，就证明存在解。

[Time]: O(n + n*cap) = O(n*cap), N为nums的元素个数，cap为(S+Sum) // 2；
[Space]: O(cap+1)
Runtime: 76 ms, faster than 98.69% of Python3 online submissions for Target Sum.
Memory Usage: 13.8 MB, less than 58.33% of Python3 online submissions for Target Sum.
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        Sum = sum(nums)
        if S > Sum or (S+Sum) % 2: return 0
        cap = (S+Sum) // 2
        dp = [0] * (cap+1)
        dp[0] = 1
        for num in nums:
            for j in range(cap, num-1, -1):
                dp[j] = dp[j] + dp[j-num]
        return dp[cap]

'''
474. Ones and Zeroes [Medium]
[题目大意]：
我们现在从数组中每个字符串都有一些0和1，问给了m个0，n个1，从数组中取出最多的字符串，这些字符串中1和0的出现次数之和不超过m，n.

[Analysis]:
遇到这种求最多或最少的次数的，并且不用求具体的解决方案，一般都是使用DP。

This problem is a typical 0-1 knapsack problem,
we need to pick several strings in provided strings to get the maximum number of strings using limited number 0 and 1.
We can create a three dimensional array, in which dp[i][j][k] means the maximum number of strings
we can get from the first i argument strs using limited j number of '0's and k number of '1's.

For dp[i][j][k], we can get it by fetching the current string i or discarding the current string,
which would result in dp[i][j][k] = dp[i-1][j-numOfZero(strs[i])][i-numOfOnes(strs[i])] and dp[i][j][k] = dp[i-1][j][k];
We only need to treat the larger one in it as the largest number for dp[i][j][k].
we cannot decrease the time complexity, but we can decrease the space complexity from ijk to j*k。

这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的字符串得最大数目。
遍历每个字符串统计出现的0和1得到zeros和ones，所以有状态转移方程：
dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
即，用i个0和j个1，在数组strs里面，求能组成的字符串的最大数目时有两种情况：
1.不算当前的字符串str，则有dp[i][j]个；
2.要算当前的字符串str,则str之前的字符串只能用i-zeros个0和j-ones个1，所得的字符串个数和为dp[i - zeros][j - ones] + 1。
因此我们比较大小，取最大的值。
其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么之前的字符串用用剩下的0和1时取的最多的数字。
边界条件：dp[0][0],表示用0个0和0个1能凑出的字符串个数为0。
[Time]: O(s*m*n)
[Space]: O(m*n)
Runtime: 2864 ms, faster than 68.16% of Python3 online submissions for Ones and Zeroes.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Ones and Zeroes.
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i - zeros][j - ones] + 1, dp[i][j])
        return dp[m][n]
