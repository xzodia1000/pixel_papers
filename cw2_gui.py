import streamlit as st
from pixel_papers.backend.builder_main import BuilderMain
from pixel_papers.gui import home, task


def main():
    st.title("Pixel Papers")

    # Initialize a 'builder' object in session state if it doesn't exist
    # The 'builder' object is presumably used for backend operations
    if "builder" not in st.session_state or st.session_state.builder is None:
        st.session_state.builder = BuilderMain()

    # Initialize the 'page' state variable to navigate between different pages of the app
    # This acts like a simple router for the Streamlit app
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    # Based on the current value of 'page' in session state,
    # display the appropriate page in the Streamlit app
    if st.session_state["page"] == "home":
        home.home()  # Display the home page

    elif st.session_state["page"] == "task":
        task.task()  # Display the task page


# Standard Python practice for running the main function
# when the script is executed directly (not imported)
if __name__ == "__main__":
    main()
