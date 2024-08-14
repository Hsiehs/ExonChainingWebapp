import random

def generate_random_exons(num_exons, max_position, max_weight):
    exons = []
    for _ in range(num_exons):
        start = random.randint(0, max_position - 1)
        end = random.randint(start + 1, max_position)
        weight = random.randint(1, max_weight)
        exons.append((start, end, weight))
    return exons

def write_exons_to_file(exons, filename):
    with open(filename, 'w') as file:
        for exon in exons:
            if (exon == exons[len(exons) - 1]):
                file.write(f"({exon[0]}, {exon[1]}, {exon[2]}) ")
            else:
                file.write(f"({exon[0]}, {exon[1]}, {exon[2]}), ")

# Example: Generate 5 random exons with maximum position 10 and maximum weight 5
random_exons = generate_random_exons(5, 10, 5)

# Write exons to a text file
write_exons_to_file(random_exons, "exons.txt")

