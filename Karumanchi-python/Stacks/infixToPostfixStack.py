class Stack:
    def __init__(self) -> None:
        self.items = []
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def __str__(self) -> str:
        return str(self.items)

    def infixToPostfix(self, exp):
        for i in exp:
            if i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    print(self.pop(), end="")
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            elif i == '+' or i == '-' or i == '*' or i == '/':
                while not self.isEmpty() and self.peek() != '(' and self.precedence(i) <= self.precedence(self.peek()):
                    print(self.pop(), end="")
                self.push(i)
            else:
                print(i, end="")

        while not self.isEmpty():
            print(self.pop(), end="")

    def precedence(self, op):
        """ 
        Return the precedence of the operator op.

        The precedence of an operator is a numerical value that determines
        the order in which operators are evaluated in an expression. The
        higher the precedence of an operator, the earlier it is evaluated.

        The precedence of the operators is as follows:

        1. * and /
        2. + and -

        If the operator is not one of the above, the precedence is 0.

        Parameters
        ----------
        op : str
            The operator for which the precedence is to be determined

        Returns
        -------
        int
            The precedence of the operator
        """
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        return 0

        
            