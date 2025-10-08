class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == "+":
                    stack.append(operand_1 + operand_2)
                if token == "-":
                    stack.append(operand_1 - operand_2)
                if token == "*":
                    stack.append(operand_1 * operand_2)
                if token == "/":
                    stack.append(int(operand_1 / operand_2))
        
        return stack[-1]