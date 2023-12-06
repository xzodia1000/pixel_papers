import os
import streamlit as st


def task():
    st.subheader("Select Task")

    # Dropdown to select a task with different options
    task_id = st.selectbox(
        "Task ID",
        [
            "1 - Python",
            "2a - Views by Country",
            "2b - Views by Continent",
            "3a/3b - Views by Browser",
            "4 - Reader Profiles",
            "5/6 - Also Likes",
        ],
    )

    # Call different functions based on the selected task
    if "1" in task_id:
        task_1()
    elif "2" in task_id:
        task_2(task_id[1])
    elif "3" in task_id:
        task_3()
    elif "4" in task_id:
        task_4()
    elif "5" in task_id:
        task_5()

    # Button to go back to the home page and reset the builder
    if st.button("Go Back"):
        st.session_state.builder = None
        st.session_state["page"] = "home"
        st.rerun()


def task_1():
    # Display a styled message using HTML and CSS
    st.markdown(
        # HTML and CSS for custom styling
        """
        <style>
            .python-info {
                color: #3776AB;
                font-family: 'Courier New', Courier, monospace;
                background-color: #262730;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #e54343;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
        <div class="python-info">
            <h2>🐍 Python 3 Power 🚀</h2>
            <p>This program was developed with the elegance of <strong>Python 3</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def task_2(task_id):
    st.subheader("Select Document")
    doc_uuid = st.text_input("Document UUID")
    chart = st.radio("Chart Type", ["Bar Chart", "Histogram"])

    # Display results based on user input and selected chart type
    if st.button("Show Results"):
        try:
            with st.spinner("Loading... (This may take a while)"):
                # Differentiate between views by country and continent
                if task_id == "a":
                    plot = st.session_state.builder.views_by_country(
                        doc_uuid, False if chart == "Bar Chart" else True
                    )
                elif task_id == "b":
                    plot = st.session_state.builder.views_by_continent(
                        doc_uuid, False if chart == "Bar Chart" else True
                    )
                st.pyplot(plot)
        except Exception as _:
            st.error("An error occurred. Please try again. Check the document UUID.")


def task_3():
    st.subheader("Select Document")
    chart = st.radio("Chart Type", ["Bar Chart", "Histogram"])

    # Display browser view results based on the selected chart type
    if st.button("Show Results"):
        try:
            with st.spinner("Loading... (This may take a while)"):
                plot = st.session_state.builder.views_by_browser(
                    hist=False if chart == "Bar Chart" else True
                )
                st.pyplot(plot)
        except Exception as _:
            st.error("An error occurred. Please try again.")


def task_4():
    if st.button("Show Results"):
        try:
            with st.spinner("Loading... (This may take a while)"):
                top_readers, time = st.session_state.builder.reader_profiles()

            # Presenting the results in two columns for better readability
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Top Readers")
                for i, reader in enumerate(top_readers):
                    st.markdown(f"**Reader {i + 1}:** {reader}")

            with col2:
                st.markdown("### Reading Time (minutes)")
                for t in time:
                    st.markdown(f"**{milliseconds_to_minutes(t):.2f}**")

        except Exception as e:
            st.error("An error occurred. Please try again.")
            st.error(e)


def task_5():
    st.subheader("Select Document and User")
    doc_uuid = st.text_input("Document UUID")
    user_uuid = st.text_input("User UUID")

    # Show results for the 'also likes' analysis
    if st.button("Show Results"):
        try:
            docs, dot = st.session_state.builder.also_likes(
                doc_uuid, user_uuid if user_uuid != "" else "user", render=False
            )
            st.markdown("### Documents")
            if len(docs) == 0:
                st.markdown("No documents found. Check the UUIDs.")
            else:
                for i, doc in enumerate(docs):
                    st.markdown(f"**Document {i + 1}:** {doc}")
                st.graphviz_chart(dot)

                # Download the graph as a PDF file
                st.download_button(
                    label="Save as .dot file",
                    data=dot.source,
                    file_name="graph.dot",
                    mime="text/plain",
                )
        except Exception as e:
            st.error("An error occurred. Please try again. Check the UUIDs.")
            st.error(e)


def milliseconds_to_minutes(milliseconds):
    """Convert milliseconds to minutes."""
    return milliseconds / (1000 * 60)
