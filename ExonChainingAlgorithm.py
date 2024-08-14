import sys
# Sorts by begining and end
def myFunc(exons):
    return exons[1], exons[0]

# Calculates maximum weight of non-overlapping exons
def ExonChaining(G, n):
    s = [0] * (n + 1) # Keep track of weight at each position
    path = [] # Used to track path
    
    # Iterate through each exon
    for i in G:
        new_val = s[i[0]] + i[2] # Calculate new value by adding exons weight to the starting position
        if s[i[1]] < new_val: # Update the end positions weight if the new value is greater
            s[i[1]] = new_val
            path.append(i) # Add the current exon to path. Can overlap, tracks each exon that changes any path
        
        # Ensure current weight is non-decreasing by filling the remainder of s with the current weight
        for j in range(i[1] + 1, n + 1):
            s[j] = max(s[j], s[j - 1])
    return s[n], path

# Removes overlapping exons leaving the best chain
def remove_overlapping_exons(path):
    non_overlapping_path = []
    i = len(path) - 1
    
    prev_begin = path[i][1]
    # If current exon ends before the last exon starts, it is non-overlapping and add to path
    while i >= 0:
        curr_exon = path[i]
        if curr_exon[1] <= prev_begin:
            non_overlapping_path.append(curr_exon)
            prev_begin = curr_exon[0]
            
        i -= 1
        
    non_overlapping_path.reverse()
    return non_overlapping_path

def main():
    exons = []
    exons_file = sys.argv[1]
    
    with open(exons_file, "r") as file:
        exons_string = file.read()
        
    exons_string = exons_string.strip()
    exons_string = exons_string.strip("()")

    # Split the string by "), (" to separate each exon
    exons_list = exons_string.split("), (")

    # Process each exon
    for exon_str in exons_list:
        # Strip any remaining parentheses and split by comma and space to get individual values
        exon_values = exon_str.strip("()").split(", ")
        # Convert values to integers and create a tuple
        exon_tuple = tuple(map(int, exon_values))
        # Add the tuple to the list of exons
        exons.append(exon_tuple)
        
    exons.sort(key=myFunc)

    find_weight, path = ExonChaining(exons, exons[len(exons) - 1][1])
    path = remove_overlapping_exons(path)

    # Write the results to a file
    with open("results.txt", "w") as file:
        file.write("Exons: ")
        for i, exon in enumerate(exons):
            if i > 0:
                file.write(", ")
            file.write(f"{exon}")
        file.write(f"\nMaximum weight: {find_weight}\n")
        file.write("Path: ")
        for i, exon in enumerate(path):
            if i > 0:
                file.write(", ")
            file.write(f"{exon}")
            
    with open("visualization.txt", "w") as file:
        for exon in exons:
            file.write(f"{exon}")

        for exon in path:
            file.write(f"{exon}")
if __name__ == "__main__":
    main()
