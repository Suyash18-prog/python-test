# Create a program that checks if the brackets (), {}, [] are balanced in an expression.

expression = "{[2+4](2*3))}"

for char in expression:
    if char=='(':
        expression.count('(')==expression.count(')')
        print("Balanced paranthesis")
    else:
        print("Imbalanced paranthesis")
    
    if char=='[':
        expression.count('[')==expression.count(']')
        print("Balanced square braces")
    else:
        print("Imbalanced square braces")

    if char=='{':
        expression.count('{')==expression.count('}')
        print("Balanced curley braces")
    else:
        print("Imbalanced curley braces")
    
