import re

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0 

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def push(self, op):
        self.stack.append(op)

class CustomPostfixEvaluator:

    def __init__(self):
        self.stack = Stack()

    def evaluate(self, a, op, b):
        match(op):
            case '+': return str(a+b)
            case '-': return str(a-b)
            case '*': return str(a*b)
            case '/': return str(a/b)
            case '^': return str(a**b)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n*self.factorial(n-1)
	
    def isOperand(self, ch):
            return ch.isalnum()
    
    # All operators are assumed to be present in the evaluate function and all operands are assumed to be numeric
    # If supplying a string, everything is assumed to be single characters with no seperators
    # If supplying a tokenized input, both operators and operands may consist of multiple characters
    def evaluatePostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.stack.push(i)
            else:
                if i == '!':
                    # Truncating may produce errors, but for this use case it should only be getting used on integers
                    val = int(float(self.stack.pop()))
                    self.stack.push(self.factorial(val))
                else:
                    val2 = float(self.stack.pop())
                    val1 = float(self.stack.pop())
                    self.stack.push(self.evaluate(val1, i, val2))
        
        return self.stack.pop()

class CustomPrefixEvaluator:

    def __init__(self):
        self.stack = Stack()

    def evaluate(self, a, op, b):
        match(op):
            case '+': return str(a+b)
            case '-': return str(a-b)
            case '*': return str(a*b)
            case '/': return str(a/b)
            case '^': return str(a**b)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n*self.factorial(n-1)
	
    def isOperand(self, ch):
            return ch.isalnum()
    
    # All operators are assumed to be explicity present in the expression and all operands are assumed to be numeric
    # If supplying a string, everything is assumed to be single characters with no seperators
    # If supplying a tokenized input, both operators and operands may consist of multiple characters
    def evaluatePrefix(self, exp):
        for i in exp[::-1]:
            if self.isOperand(i):
                self.stack.push(i)
            else:
                if i == '!':
                    # Factorial is meant to only work on integers, so truncating here shouldn't produce errors if used correctly
                    val = int(float(self.stack.pop()))
                    self.stack.push(self.factorial(val))
                else:
                    val1 = float(self.stack.pop())
                    val2 = float(self.stack.pop())
                    self.stack.push(self.evaluate(val1, i, val2))
        
        return self.stack.pop()


class InfixToPostfixConverter:

    def __init__(self):
        self.stack = Stack()
        self.precedence = {'(': 0, ')': 0,'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, "!": 4}

    def isOperand(self, ch):
        return ch.isalnum()

    def notGreater(self, i):
        return self.precedence[i] <= self.precedence[self.stack.peek()]

    # All operators are assumed to be present in the precedence dictionary and all operands are assumed to be alphanumeric
    # If supplying a string, everything is assumed to be single characters with no seperators
    # If supplying a tokenized input, both operators and operands may consist of multiple characters
    def infixToPostfix(self, exp):
        output = []
        for i in exp:
            if self.isOperand(i):
                output.append(i)

            elif i == '(':
                self.stack.push(i)

            elif i == ')':
                while((not self.stack.isEmpty()) and
                    self.stack.peek() != '('):
                    a = self.stack.pop()
                    output.append(a)
                if (not self.stack.isEmpty() and self.stack.peek() != '('):
                    return -1
                else:
                    self.stack.pop()

            else:
                while(not self.stack.isEmpty() and self.notGreater(i)):
                    output.append(self.stack.pop())
                self.stack.push(i)

        while not self.stack.isEmpty():
            output.append(self.stack.pop())

        return output

class InfixToPrefixConverter:

    def __init__(self):
        self.stack = Stack()
        self.toPostfix = InfixToPostfixConverter()
        self.precedence = {'(': 0, ')': 0,'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, "!": 4}

    def isOperand(self, ch):
        return ch.isalnum()

    def notGreater(self, i):
        return self.precedence[i] < self.precedence[self.stack.peek()]
    
    def reverse(self, exp):
        result = []
        for c in exp[::-1]:
            if c == "(":
                result.append(")")
            elif c == ")":
                result.append("(")
            else:
                result.append(c)
        return result

    # "Reverse" input expression, convert to pseudopostfix with a slightly different precedence eval, then "reverse" the result
    # Since this uses the postfix converter, all the same assumptions apply to the expression here as above
    def infixToPrefix(self, exp):
        output = []
        for i in self.reverse(exp):
            if self.isOperand(i):
                output.append(i)

            elif i == '(':
                self.stack.push(i)

            elif i == ')':
                while((not self.stack.isEmpty()) and
                    self.stack.peek() != '('):
                    a = self.stack.pop()
                    output.append(a)
                if (not self.stack.isEmpty() and self.stack.peek() != '('):
                    return -1
                else:
                    self.stack.pop()

            else:
                while(not self.stack.isEmpty() and self.notGreater(i)):
                    output.append(self.stack.pop())
                self.stack.push(i)

        while not self.stack.isEmpty():
            output.append(self.stack.pop())

        return self.reverse(output)

if __name__ == '__main__':
    postf = InfixToPostfixConverter()
    poev = CustomPostfixEvaluator()

    found = 0
    with open("test.txt", "r") as file:
        for line in file:
            string = line.rstrip().split(" ")[-1]
            if string != "Impossible":
                # Capturing delimiters inserts empty strings
                tokens = [x for x in re.split('([^a-zA-Z0-9])', string) if x != ""]
                postfix = postf.infixToPostfix(tokens)
                val = poev.evaluatePostfix(postfix)
                if float(val) == 24.0:
                    continue
                found += 1 
                print(string,"=",val)

    if found == 0:
        print("All equations correct")
    else:
        print("{} equations incorrect".format(found))