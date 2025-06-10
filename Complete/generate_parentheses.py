class Solution:
    

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen_p(n, open_p, close_p, stack):
            # base case
            if open_p == close_p == n:
                res.append("".join(stack))

            # add open
            if open_p < n:
                stack.append("(")
                gen_p(n, open_p + 1, close_p, stack)
                stack.pop()

            # add close
            if close_p < open_p:
                stack.append(")")
                gen_p(n, open_p, close_p + 1, stack)
                stack.pop()

        gen_p(n, 0, 0, [])

        return res


