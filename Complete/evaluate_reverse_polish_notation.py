class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # if number else operator
            try:
                t = int(t)
                stack.append(t)
            except ValueError:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(int(a + b))
                elif t == "-":
                    stack.append(int(a - b))
                elif t == "/":
                    stack.append(int(a / b))
                elif t == "*":
                    stack.append(int(a * b))
        
        return stack.pop()