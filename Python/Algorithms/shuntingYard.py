class PostFix:
    @staticmethod
    def convert(expression):
        final_str = ''
        stack = []
        prec = {'(': 0, '+': 1, '*': 2, '/': 2, '-': 3}

        for i in expression:
            if(i.isalpha()):
                final_str += i
            elif(i == '('):
                stack.append(i)
            elif(i == ')'):
                topOp = stack.pop()
                while (topOp != '('):
                    final_str += topOp
                    topOp = stack.pop()
            else:
                while(len(stack) > 0 and
                      prec[stack[-1]] >= prec[i]):
                    final_str += stack.pop()
                stack.append(i)

        while(len(stack) > 0):
            topOp = stack.pop()
            final_str += topOp

        return final_str

    @staticmethod
    def evaluate(expression):
        stack = []
        expression = expression.split()
        for i in expression:
            if(i.isdigit()):
                stack.append(float(i))
            elif(i == '+'):
                stack.append(stack.pop() + stack.pop())
            elif(i == '-' and len(stack) > 0):
                term2 = stack.pop()
                term1 = stack.pop() if len(stack) > 0 else 0
                result = term1 - term2 if term1 != 0 else -term2
                stack.append(result)
            elif(i == '*'):
                stack.append(stack.pop() * stack.pop())
            elif(i == '/'):
                term2 = stack.pop()
                term1 = stack.pop()
                stack.append(term1/term2)
            else:
                raise Exception('Unknown character "%s" cannot be evaluated' %i)
        return stack.pop()
