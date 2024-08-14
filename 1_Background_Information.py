import streamlit as st

def background_information():
    st.set_page_config(
        page_title="Background Information",
        page_icon=":book:",
    )

    st.markdown("# Background Information")
    st.sidebar.success("Background Information")

    st.header("What are we trying to solve?")
    st.markdown(
        """
        Given a set of non-putative exons, find a maximum set of non-overlaping putative exons.
    """
    )

    st.header("How do we solve it?")
    st.markdown(
        """
        We solved this problem using dynamic programming, which allows us to break down the problem into
        simpler steps.
    """
    )
    st.markdown("1. **Process the input data**")
    st.markdown("2. **Dynamic programming to find maximum weight of Non-Overlapping Exons**")
    st.markdown("3. **Path tracking**")
    st.markdown("4. **Remove overlapping exons to find the optimal chain**")
    st.markdown("5. **Output the data**")

    st.header("What is the graph representation?")
    st.markdown(
        """
        The graph representation is a critical learning tool for our solution. The nodes on the
        graph represent potential exons. The nodes consist of its start and end positions within
        the genome, and the weight (start, end, weight). The weight of the node represents its biological significance
        of the exon sequence. Using the graph we can identify the most significant non-overlapping
        sequence of exons.
    """
    )

    st.header("File formatting")
    st.markdown(
        """
        The exons are in tuple format. Each tuple contains three integers that represent the start, end, and weight: (start, end, weight).
        Between each of start, end, and weight is a comma and a space as shown. Each exon is separated by a comma and space: (1, 3, 5), (2, 7, 1).
        Example file formatting is shown in Figure 1. The visualization supports up to 15 exons when fully expanded, and 5 when minimized, 
        but there is no limit to the number of exons that the default output can support.
    """
    )
    st.markdown(
        """
        Figure 1:
    """
    )
    st.header("(4, 5, 4), (0, 2, 2), (8, 10, 4), (6, 7, 5), (8, 10, 3)")

    st.header("Additional Information")
    st.markdown(
    """
        For an in-depth exploration of the topics discussed here, consider the following resources:

        - **Exons and Gene Structure**: To understand the fundamental role of exons within the gene structure, 
        [Nature Education's Scitable](https://www.nature.com/scitable/topicpage/gene-expression-14121669/) provides an excellent overview.

        - **Exon Chaining Algorithm**: For a technical deep dive into the exon chaining algorithm, the lecture slides available at [University of North 
        Carolina's Computer Science department](http://www.cs.unc.edu/~prins/Classes/555/Media/Lec11.pdf) offer a comprehensive overview.

        Should you seek information beyond what is provided in these resources or wish to deepen your understanding further, 
        university bookstores and libraries are treasure troves of academic literature and textbooks covering a wide range of topics in genetics and bioinformatics. 
        Additionally, the internet hosts an abundance of educational videos. Platforms like YouTube, Khan Academy, and Coursera offer lectures, tutorials, and course 
        materials.
    """
    )

background_information()
