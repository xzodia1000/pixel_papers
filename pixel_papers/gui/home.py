import streamlit as st


def home():
    st.subheader("Upload file")

    # Create a file uploader widget allowing json file types
    file = st.file_uploader("Choose a file", type=["json"])

    # Checkbox to allow user to choose a default file
    default_file = st.checkbox("Use default file (sample_small.json ~ 10K lines)")

    # Check if a file has been uploaded or the default file checkbox is checked
    if file is not None or default_file:
        # Create a button named 'Next'
        if st.button("Next"):
            # If the default file checkbox is checked
            if default_file:
                # Show a spinner while the file is being loaded
                with st.spinner("Loading... (This may take a while)"):
                    # Read the default file using the builder's read_file method
                    st.session_state.builder.read_file()
                st.success("Done!")
            else:
                # Show a spinner while the file is being loaded
                with st.spinner("Loading... (This may take a while)"):
                    # Read the uploaded file using the builder's read_file method
                    st.session_state.builder.read_file(file)
                st.success("Done!")

            st.session_state[
                "page"
            ] = "task"  # Set the page in session state to "task" for navigation
            st.rerun()  # Rerun the Streamlit script to reflect the changes in the session state
