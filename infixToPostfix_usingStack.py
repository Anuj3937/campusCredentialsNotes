def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    for char in expression:
        if char.isalnum(): 
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            while (stack and stack[-1] != '(' and 
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)
def main():
    while True:
        try:
            expression = input("\nEnter an infix expression (or 'quit' to exit): ").strip()  
            if expression.lower() == 'quit':
                print("GoodNight buddy!")
                break
            if not expression:
                print("Please enter a valid expression.")
                continue
            expression = expression.replace(' ', '')   
            postfix = infix_to_postfix(expression)
            prefix = list(postfix)
            a=prefix[::-1]
            b=''.join(a)
            print(f"Infix expression:  {expression}")
            print(f"Postfix expression: {postfix}")
            print(f"Prefix expression: {b}")
        except Exception as e:
            print(f"enter a valid expression {e}")
if __name__ == "__main__":
    main()
