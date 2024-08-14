import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Exon Chaining Algorithm Visualization",
        page_icon="🧬",
    )

    st.title("Exon Chaining Algorithm Visualization")

    st.sidebar.success("Select: Background | Algorithm Visualization")

    st.header("Welcome to the Exon Chaining Visualization Tool")
    st.markdown(
        """
        Learn the exon chaining algorithm for gene research through interactive
        visualization. Designed for biologists, researchers and students, this
        tool demonstrates the Exon Chaining algorithm in a user-friendly way.
    """
    )

    st.header("Background")
    st.markdown(
        """
        Explore our step-by-step guide to gain the required knowledge to understand exon chaining.
    """
    )

    st.header("Algorithm Visualization")
    st.markdown(
        """
        Input your own data and see the exon chaining algorithm in action. Upload your
        data or use the data we generate to get started. The algorithm transforms the data into
        an understandable graph representation.
    """
    )

if __name__ == "__main__":
    run()
