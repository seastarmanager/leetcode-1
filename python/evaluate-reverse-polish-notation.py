class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):

        def calc (left, right, operator):
            left = int(left)
            right = int(right)
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return int(float(left) / right)
        
        temp_stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                right = temp_stack.pop()
                left = temp_stack.pop()
                temp_stack.append(calc(left, right, token))
            else:
                temp_stack.append(token)
        
        return int(temp_stack[0])