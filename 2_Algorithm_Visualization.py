import streamlit as st
import os
import subprocess
import pandas as pd
import numpy as np


# Function to generate random exons using the provided Python script
def generateRandomExons():
    # Replace "random_exon_generator.py" with the name of your random exon generator script
    subprocess.run(["python", "RandomExonGenerator.py"])
    with open("exons.txt", "r") as file:
        randomExons = file.readlines()
    return randomExons

# Function to run the algorithm with the generated exons
def runAlgorithm(exons_file):
    # Replace "exon_algorithm.py" with the name of your exon chaining algorithm script
    subprocess.run(["python", "ExonChainingAlgorithm.py", exons_file])

    with open("results.txt", "r") as file:
        algorithmResults = [line.strip() for line in file.readlines()]
    return algorithmResults

def readFile(visualization_file):
    exons = []
    path = []
    seen = {}

    with open(visualization_file, "r") as file:
        exons_string = file.read()
        exons_list = exons_string.split(")(")

    for exon in exons_list:
        exon_values = exon.strip("()").split(",")
        exon_tuple = tuple(map(int, exon_values))
        
        if exon_tuple in seen:
            path.append(exon_tuple)
        else:
            seen[exon_tuple] = len(exons)
            exons.append(exon_tuple)
    
    colors = ["#00FFFF" if exon not in path else "#ff0000" for exon in exons]
    return exons, colors

def dataFrameCreation(exon_list):
    y = {}
    
    max_value = max(exon[1] for exon in exon_list)
    b_values = [i for i in range(max_value + 1)]
    ascii_base = ord('A')
    
    for exon_index in range(len(exon_list)):
        keyString = f"Exon {chr(ascii_base + exon_index)}: {exon_list[exon_index]}"
        y[keyString] = [None] * (max_value + 1)
        for i in range(exon_list[exon_index][0], exon_list[exon_index][1] + 1):
            y[keyString][i] = exon_index

    exon_df = pd.DataFrame(y, index = b_values)
    return exon_df

        
def main():
    st.set_page_config(
        page_title="Algorithm Visualization",
        page_icon=":chart_with_upwards_trend",
    )

    st.markdown("# Algorithm Visualization")
    st.sidebar.success("Algorithm Visualization")

    # Allow user to upload a file
    uploadedFile = st.file_uploader("Upload Exon File", type=["txt"])

    # Button to trigger random exon generation
    if st.button("Generate Random Exons"):
        randomExons = generateRandomExons()
        st.write("Generated Random Exons:")
        for exon in randomExons:
            st.write(exon.strip())
            
    # Button to run the program
    if st.button("Run Algorithm"):
        if uploadedFile is not None:
            # Save the uploaded file
            with open("uploaded_exons.txt", "wb") as file:
                file.write(uploadedFile.getvalue())
            exons_file = "uploaded_exons.txt"
        else:
            # Use the default random exons file
            exons_file = "exons.txt"

        # Run the algorithm with the specified exons file
        results = runAlgorithm(exons_file)

        # Display the results
        st.write(results)

        st.markdown("Red highlights the best path of non-overlapping putative exons, with the remaining exons in blue.")
        exons, colors = readFile("visualization.txt")
        df = dataFrameCreation(exons)
        st.line_chart(df, color=colors)
        

# Run the app
if __name__ == "__main__":
    main()
