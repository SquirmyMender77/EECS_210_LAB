# Name: Preston Dahl
# KUID:[ID REDACTED]
# Lab session: M4:30
# Lab #4
# Description: 
# 
# Collaborators: 
# Outside sources: 

#Function to get b, n, and m
#They should all be on the same line
#If you want, you can put commas in between
def get_values():
    i = input("Please enter b, n, and m: ")
    items = i.replace(","," ").split()
    if(len(items) != 3):
        print("Invalid input, try again")
        return get_values()
    return (int(items[0]),int(items[1]),int(items[2]))

#For the output, you can just print the number:
# e.g. print(result)

#Your code here:
def main():
    b, n, m = get_values()
    x = 1
    power = b % m
    k=bin(n).replace("0b","")
    k=k[::-1]
    for digit in k:
        if digit=="1":
            x = (x*power) % m
        power = (power*power) % m
            
    return (print(x))

k=main()
