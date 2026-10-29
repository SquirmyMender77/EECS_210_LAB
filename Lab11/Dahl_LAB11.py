# Name:Preston Dahl
# KUID:[ID REDACTED]
# Lab session: M 4:30
# Lab #:11
# Description: This program converts a prefix expression into a postfix expression by reversing the prefix expression and appending the characters x,y,z,1,2,3 first
# and then taking the top two stack values when an operator is reached.
#
# Collaborators: None
# Outside sources: None

def get_postfix_expr():
    valid_ops = ["+", "-", "*", "/", "^"]
    valid_nums = ["1", "2", "3"]
    valid_vars = ["x", "y", "z"]
    loop = True
    while loop:
        loop = False
        pf_input = input("Enter an arithmetic expression in postfix form: \n")
        split_input = pf_input.split(" ") # Split the line into a list of characters
        for char in split_input:
            if char not in valid_nums and char not in valid_vars and char not in valid_ops:
                print("Invalid input.")
                loop = True
                break
    return pf_input

def postfix_conversion():
    Stack = []
    postfix = get_postfix_expr()
    read = postfix[::-1]
    for i in read:
        if i  in ["x", "y", "z", "1", "2", "3"]:
            Stack.append(i)
        elif i in ["^", "*", "/", "+", "-"]: 
            operator = i
            
            operand1 = Stack.pop()
            operand2 = Stack.pop()
            new_string = operand1 + operand2 + operator
            Stack.append(new_string)
    return Stack
m = postfix_conversion()
for i in m:
    print(i)
