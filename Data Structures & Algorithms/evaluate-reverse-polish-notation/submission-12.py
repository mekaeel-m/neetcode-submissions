class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for i in range(len(tokens)):
            
            if tokens[i] in '+-*/':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(self.evalFunc(num1,num2,tokens[i]))
            else:
                num_stack.append(int(tokens[i]))
        
        return num_stack[0]

        
    def evalFunc(self,numOne: str,numTwo: str,operand) -> int:
        num1 = int(numOne)
        num2 = int(numTwo)

        if operand == '+':
            return num1 + num2
        elif operand == '-':
            return num1 - num2
        elif operand == '*':
            return num1 * num2
        elif operand == '/':
            if num2 == 0:
                raise ValueError("Division by zero")
            return int(num1 / num2)
        else:
            raise Error
        