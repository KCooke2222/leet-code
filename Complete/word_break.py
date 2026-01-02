class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # iterate over s check if is in dict each time
        # issue may jump the gun adding a smaller string when is better to use longer one
        # fix each time can add something create new dfs search for optimal solution
        # use memo on positions

        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            check_str = ""
            for c in range(len(s) - i):
                check_str += s[i + c]
                if check_str in wordDict: # go both ways add and don't add (in case better option)
                    if dfs(i + len(check_str)): # new path
                        memo[i] = True
                        return True 

            memo[i] = False
            return False # no complete path found
                    

        return dfs(0)