def myFunc(exons):
    return exons[1]

# Function to find the closest exon for each exon
def find_closest_exon(exons):
    closest_exons = []

    # Loop through each exon
    for i in range(len(exons)):
        current_exon = exons[i]
        current_start = current_exon[0]
        closest_index = 0  # Default to the first exon

        # Loop through the exons before the current one
        for j in range(i):
            prev_exon = exons[j]
            prev_end = prev_exon[1]
            
            # Ensure that the current exon starts after the end of the previous exon
            # and its start position is closer to the current start position than the previously found closest exon
            if current_start >= prev_end and current_start - prev_end <= current_start - exons[closest_index][1]:
                closest_index = j + 1  # Adjusted to +1 as we're indexing from 0

        closest_exons.append(closest_index)

    return closest_exons

# Function to find the maximum cumulative weight
def find_max_weight(closest_exons, exons):
    weights = [0]
    # Loop through each exon
    for i in range(0, len(exons)):
        # Calculate the maximum cumulative weight for the current exon
        weights.append(max(weights[i], exons[i][2] + weights[closest_exons[i]]))
    return weights

def find_path(max_weight_index, closest_exons):
    path = []
    index = max_weight_index - 1
    while index > 0:
        path.append(index)
        index = closest_exons[index]
        
    path.reverse()
    return path

def print_path(path):
    print("Path: ", exons[path[0]], end="")
    for i in range(1, len(path)):
        print(", ", exons[path[i]], end="")
        
# Example input
exons = [(0, 1, 1), (7, 8, 2), (0, 3, 2), (2, 4, 2), (2, 6, 2), (5, 8, 3)]
exons.sort(key=myFunc)
# Finding closest exons
closest_exons = find_closest_exon(exons)

# Finding maximum cumulative weight
weights = find_max_weight(closest_exons, exons)

# Printing the maximum cumulative weight]
print("Exons: ", exons)
print("Closest Excons: ", closest_exons)
print("Weights: ", weights)
max_weight_index = weights.index(max(weights))
print_path(find_path(max_weight_index, closest_exons))
print("Max Weight: ", max(weights))

