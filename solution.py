

# O(n)
def resolve_optimized(l):
    mult = 1
    
    zeros = 0 
    index = 0

    #descovers the number of zeros in the entry list
    for i in range(len(l)):
        if l[i] == 0:
            zeros = zeros + 1
            index = i
    
    # if there are no zeroes, run the optimized solution:
    if zeros == 0:
        o = []
        for i in range(len(l)):
            mult = mult * l[i]
        for i in range (len(l)):
            current = l[i]
            if(current != 0):
                o.append(int(mult/current))
        return o
    
    # if there is one zero, only that position will have a value different from 0:
    elif zeros == 1:
        o = [0 for x in range(len(l))] # creates a list of zeroes
        mult = 1
        for i in range(len(l)):
            if i != index:
                mult = mult * l[i]
        o[index] = mult
        return o
   

    else:
        return [0 for x in range(len(l))]

    
# O(n²)
def resolve_not_optimized(l):
    o = []
    for i in range(len(l)):
        mult = 1
        for j in range(len(l)):
            if(i!=j):
                mult = mult * l[j]
        o.append(mult)
    return o

def main():

    # tests:

    # One zero
    print("Tests:")

    print("1:")
    I = [1,0,3,4]
    print("One zero", I)
    print("- optimized:     ", resolve_optimized(I))
    print("- not optimized: ", resolve_not_optimized(I)) 
    print("------------------------------")
    print("Expected: ", [0, 12, 0, 0]) 

    # Two zeroes
    print("2:")
    I = [1,0,3,0]
    print("Two zeroes", I)
    print("- optimized:     ", resolve_optimized(I))
    print("- not optimized: ", resolve_not_optimized(I)) 
    print("------------------------------")
    print("Expected: ", [0, 0, 0, 0]) 

    # Zero zeroes
    print("3:")
    I = [1,10,3,6]
    print("Two zeroes", I)
    print("- optimized:     ", resolve_optimized(I))
    print("- not optimized: ", resolve_not_optimized(I)) 
    print("------------------------------")
    print("Expected: ", [180, 18, 60, 30])

if __name__ == "__main__":
    main()