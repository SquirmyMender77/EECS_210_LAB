# EECS 210 Lab 1
# Preston Dahl
# Collaborators: No external Sources used.
# Lab Session: Monday 4:30
# Lab assignment: 01
# Description: This program takes two bitstrings of length n and utilizes 3
#              functions to output the calculations of bitwise AND, OR, and XOR.

def get_binary_string() -> str  :
    x = input("Enter a binary string: ")
    if x.replace("1","").replace("0",""):
        print("Invalid characters, please try again")
        return get_binary_string()
    return x

def pretty_print(and_result:str, or_result:str, xor_result:str) -> None:
    print(f"AND:\t{and_result}\nOR:\t{or_result}\nXOR:\t{xor_result}")
# My Code:

binary_1=get_binary_string()
binary_2=get_binary_string()

def and_result(binary_1,binary_2):
    new_binary_1=[]
    for digit_1, digit_2 in zip(binary_1, binary_2):
        if digit_1=="1" and digit_2=="1":
            result_1="1"
            new_binary_1.append(result_1)
        elif digit_1=="0" or digit_2=="0":
            result_2="0"
            new_binary_1.append(result_2)
    clean_new_binary_1="".join(new_binary_1)
    return clean_new_binary_1
and_bits=and_result(binary_1,binary_2)

def or_result(binary_1,binary_2):
    new_binary_2=[]
    for digit_1,digit_2 in zip(binary_1,binary_2):
        if digit_1=="1" or digit_2=="1":
            result_3="1"
            new_binary_2.append(result_3)
        elif digit_1=="0" and digit_2=="0":
            result_4="0"
            new_binary_2.append(result_4)
    clean_new_binary_2="".join(new_binary_2)
    return clean_new_binary_2
or_bits=or_result(binary_1,binary_2)

def xor_result(binary_1,binary_2):
    new_binary_3=[]
    for digit_1,digit_2 in zip(binary_1,binary_2):
        if digit_1=="1" and digit_2=="0":
            result_5="1"
            new_binary_3.append(result_5)
        elif digit_1=="0" and digit_2=="1":
            result_6="1"
            new_binary_3.append(result_6)
        elif digit_1=="0" and digit_2=="0":
            result_7="0"
            new_binary_3.append(result_7)
        elif digit_1=="1" and digit_2=="1":
            result_8="0"
            new_binary_3.append(result_8)
    clean_new_binary_3="".join(new_binary_3)
    return clean_new_binary_3
xor_bits=xor_result(binary_1,binary_2)
pretty_print(and_bits,or_bits,xor_bits)
