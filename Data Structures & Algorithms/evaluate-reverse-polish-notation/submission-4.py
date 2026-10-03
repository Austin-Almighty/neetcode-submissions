class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack: list[str] = []
        
        for token in tokens:
            if token in operators:
                num2, num1 = stack.pop(), stack.pop()
                match token:
                    case "+":
                        stack.append(num1+num2)
                    case "-":
                        stack.append(num1-num2)
                    case "*":
                        stack.append(num1*num2)
                    case "/":
                        stack.append(int(num1/num2))
            else:
                stack.append(int(token))

        return stack[0]