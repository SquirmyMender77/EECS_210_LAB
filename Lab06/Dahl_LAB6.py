# Name: Prston Dahl
# KUID: [ID REDACTED]
# Lab session: M 4:30PM
# Lab #6
# Description:
#
# Collaborators:
# Outside sources:

#Function converts a valid user input into a list of ints
#Does not allow the user to input repeated digits or anything that is not a number
def get_input():
    while True:
        num_str = input("Enter a number with no repeated digits: ")

        #Check that all characters are digits
        if not num_str.isdigit():
            print("Input must be a number.")
            continue

        #Check for repeated digits
        if len(set(num_str)) != len(num_str):
            print("Number must not have repeated digits.")
            continue

        #Convert to list of integers
        digits = [int(ch) for ch in num_str]
        '''
        #Check if it's the last permutation
        if all(digits[i] >= digits[i+1] for i in range(len(digits)-1)):
            print("Input is the last permutation, no next permutation exists.")
            continue
        '''
        return digits  # only returns once input is valid


def main():
    #Input Example
    num_list = get_input()
    print(num_list)
    return num_list
num_list=main()


def rearrange_to_next_biggest_number(num_list):
    n= len(num_list)-1
    j=n-1
    while j>=0 and num_list[j]>=num_list[j+1]:
        j-=1
    if j==-1:
        return None
    k=n 
    while num_list[j]>num_list[k]:
        k-=1
    num_list[j], num_list[k] = num_list[k],num_list[j]
    r=n
    s=j+1
    while r>s:
        num_list[r], num_list[s] = num_list[s], num_list[r]
        r -= 1
        s += 1
    return print(num_list)
rearrange_to_next_biggest_number(num_list)
