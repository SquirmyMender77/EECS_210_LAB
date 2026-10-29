# EECS 210 Lab 1
# Preston Dahl
# Collaborators:
#Lab Session: Monday 4:30
#Lab Assignemnt: 02
#Description: Need to write a program that determines if a mapping is a function, is one-to-one, and is onto.
#             The program takes an input n mappings of elements from set
#             {0, 1, 2, 3} to elements of set {A, B, C, D}, in the form of pairs.
#
# Note: if you are working in python, you are
# REQUIRED to call this function to get your
# input, so all assignments are consistant
# Returns a list of number,letter pairs
def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(","").replace(" ","").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs
#My Code:
pair_list = get_mapping_pairs()
def is_function(pair_list):
    maybe_Function=("Function")
    for input_1 in range(len(pair_list)):
        for input_2 in range((input_1)+1, len(pair_list)):
            if pair_list[input_1][0]==pair_list[input_2][0]:
                maybe_Function=("Not a Function")
    return maybe_Function
FUNC=is_function(pair_list)
def is_one_to_one(pair_list):
    maybe_one_to_one=(",One-to-One")
    for input_1 in range(len(pair_list)):
        for input_2 in range((input_1)+1, len(pair_list)):
            if pair_list[input_1][1]==pair_list[input_2][1]:
                maybe_one_to_one=(",Not One-to-One")
    if FUNC==("Not a Function"):
        maybe_one_to_one=("")
    return maybe_one_to_one
ONE=is_one_to_one(pair_list)
def is_onto(pair_list):
    output_values=[]
    maybe_onto=(",Not Onto")
    for output in range(len(pair_list)):
        (output_values).append(pair_list[output][1])
    if "A" in output_values and "B" in output_values and "C" in output_values and "D" in output_values:
        maybe_onto=(",Onto")
    elif FUNC==("Not a Function"):
        maybe_onto=("")
    return maybe_onto
ON=is_onto(pair_list)
print(f"{FUNC}{ONE}{ON}")
