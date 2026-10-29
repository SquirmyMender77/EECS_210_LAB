import re
def get_input_list(prompt="Enter numbers (use spaces and/or commas): ") ->list[int]:
    user_input = input(prompt)
    # Split on commas or spaces (one or more of them)
    tokens = re.split(r"[,\s]+", user_input.strip())
    # Convert to integers, ignoring empty strings
    return [int(t) for t in tokens if t]

# Example usage
def main():
    L= []
    L1 = get_input_list()
    L2 = get_input_list()
    i=0
    j=0
    while i < len(L1) and j < len(L2):
        if L1[i]<L2[j]:
            L.append(L1[i])
            i += 1
        elif L2[j]<L1[i]:
            L.append(L2[j])
            j += 1
        elif L1[i]==L2[j]:
            L.append(L1[i])
            i += 1
            j += 1
    if i < len(L1):
        L.extend(L1[i:])
    elif j < len(L2):
        L.extend(L2[j:])
            
                    
            
    return L
                
                
                    
                    
    
p=main()
print(p)
