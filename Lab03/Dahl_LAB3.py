# EECS 210 Lab 1
# Preston Dahl
# Collaborators:
#Lab Session: Monday 4:30
#Lab Assignemnt: 02
#Description:
# Returns a matrix in standard matrix notation:
# M[x][y] is row x, (top to bottom, starting at 0)
# and column y (left to right, starting at 0)
# for example, a 3x3 matrix is
# |(0,0) (0,1) (0,2)|
# |(1,0) (1,1) (1,2)|
# |(2,0) (2,1) (2,2)|
def get_matrix(ints=False):

    print("Enter a matrix consisting of zeros and ones, spaced out, same number of rows and columns, and with a blank line to end:")
    x = input()
    items = x.replace(","," ").split()
    length = len(items)
    matrix = []
    while(x.strip()):
        items = x.replace(","," ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
        else:
            if not ints:
                matrix.append(items)
            else:
                row = []
                for entry in items:
                    row.append(int(entry))
                matrix.append(row)
        x = input()
    return matrix

Rows = get_matrix()
g = get_matrix()

def get_matrix_2_column_data(g):
    column_data=list(zip(*g))
    return column_data

Columns=get_matrix_2_column_data(g)

def matrix_multiplication(Columns,Rows):
    matrix = []
    for row in Rows:
        inside_row = []
        for column in Columns:
            found = False
            for i in range(len(row)):
                if row[i] == "1" and column[i] == "1":
                    found = True
                    break
            if found == True:
                inside_row.append(1)
            elif found == False:
                inside_row.append(0)
            else:
                print("You didn't follow instructions, try again.")
            
        matrix.append(inside_row)
    return matrix
q=matrix_multiplication(Columns,Rows)
#Helper function to print a 2-D matrix
def print_matrix(q):
    for row in q:
        for item in row:
            print(item, end=" ")
        print()
print("Here comes your new matrix.")
print_matrix(q)
print("TA DA!")
user_input=(input("Isn't it beautiful?(y/n): ")).lower()

def rating_my_work(user_input):

    if user_input == "n":
        print(":(")
    elif user_input == "y":
        print(" :) ")
    else:
        print(":/")
rating_my_work(user_input)
