class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # store indices on stack
        res = [0] * len(temps)

        for d in range(len(temps) - 1):
            # compare to next day
            if temps[d] < temps[d + 1]:
                res[d] = 1

                # also check the stack
                while stack and temps[stack[-1]] < temps[d + 1]:
                    d_old = stack[-1]
                    res[d_old] = d + 1 - d_old # add difference from hotter day
                    stack.pop()
            else:
                stack.append(d) # add day to stack

        return res
