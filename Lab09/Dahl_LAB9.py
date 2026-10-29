# Name: Preston Dahl
# KUID: [ID REDACTED]
# Lab session: M 4:30
# Lab #9
# Description:
#
# Collaborators:
# Outside sources:

#This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
def get_square_matrix(ints=False):
    """ 
    Takes a square matrix of numbers from the user. Each row can be 
    separated by commas and/or spaces. Automatically ends after the last row.

    If ints=False, the function returns a matrix of strings. 
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix:")
    matrix = []

    x = input()
    #If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)

    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    #Save the first row
    if not ints:
        matrix.append(items)
    else:
        try:
            row = [int(entry) for entry in items]
            matrix.append(row)
        except ValueError:
            print("Error: all entries must be numbers! Try again:")
            #If first row is bad, try again
            return get_square_matrix(ints=ints)

    #Get the rest of the rows
    while True:
        x = input()
        items = x.replace(",", " ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            continue  # re-try the line
        if not ints:
            matrix.append(items)
        else:
            try:
                row = [int(entry) for entry in items]
                matrix.append(row)
            except ValueError:
                print("Error: all entries must be numbers! Try again:")
                continue  # re-try the line
        #Check if matrix has been completed (is square)
        if len(matrix) == length:
            return matrix

#Helper function to print a 2-D matrix
def print_matrix(m):
    n = len(m)
    # Create labels (a, b, c, ...)
    labels = [chr(ord('a') + i) for i in range(n)]
    
    # Print top header row
    print("  ", end="")  # space for corner
    for label in labels:
        print(label, end=" ")
    print()
    
    # Print each row with its corresponding label
    for i, row in enumerate(m):
        print(labels[i], end=" ")  # row label
        for item in row:
            print(item, end=" ")
        print()

def main():
    M_R = get_square_matrix(ints=True)
    n = len(M_R)
    reachability = M_R
    current_power = M_R
    
    for k in range(2, n):
        new_matrix = []
        for i in range(n):
            row_4_nm = []
            for j in range(n):
                sum1 = 0
                for m in range(n):
                    sum1 += current_power[i][m] * M_R[m][j]
                if sum1>0:
                    reachability[i][j] = 1
                row_4_nm.append(sum1)
            new_matrix.append(row_4_nm)
    current_power = new_matrix
    is_connected = True
    for i in range(n):
        for j in range(n):
            if i != j and reachability[i][j] == 0:
                is_connected = False
    if is_connected == True:
        print("connected")
    else:
        print("not connected")             
main()
