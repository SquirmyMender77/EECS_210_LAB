# Name: Preston Dahl
# KUID: [ID REDACTED]
# Lab session: M 4:30PM
# Lab #7
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



def main():
    M_R = get_square_matrix(ints=True)
    A = M_R
    B = M_R
    for row in A:
        n = len(row)
        break
    for step_counter in range(2,n+1):
        new_matrix=[]
        for i in range(len(A)):
            row_index = i
            row_4_nm = []
            for j in range(len(A[i])):
                col_index = j
                entry = 0
                for k in range(0,n):
                    entry = entry or ((A[i][k]) and (M_R[k][j]))
                    if entry == 1:
                        break
                
                row_4_nm.append(entry)
            new_matrix.append(row_4_nm)
        A = new_matrix
        B_final = []
        for i in range(len(B)):
            row_index = i
            B_row = []
            for j in range(len(B[i])):
                col_index = j
                B_row.append((B[i][j]) or (A[i][j]))
            B_final.append(B_row)
        B = B_final
    print("___Transitive Closure Matrix___")
    for row in B_final:
        print(*row)
B = main()
