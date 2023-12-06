import numpy as np
import pandas as pd
from user_agents import parse


class DataReader:
    def __init__(self):
        """
        Initialize the DataReader with an empty DataFrame.
        """

        self.df = None

    def read_data(self, path="./datasets/sample_small.json"):
        """
        Read data from a JSON file into the DataFrame.

        Args:
            path (str): The file path to the JSON data file. Defaults to "./datasets/sample_small.json".
        """

        self.df = pd.read_json(path, lines=True)

    def get_df(self):
        """
        Get the DataFrame loaded in the DataReader.

        Returns:
            DataFrame: The loaded DataFrame.
        """

        return self.df

    def get_countries(self, doc_id):
        """
        Get the count of visits per country for a specific document.

        Args:
            doc_id (str): The ID of the document to filter by.

        Returns:
            tuple: A tuple containing 3 elements:
                    - A dataframe with all entries for the specified document.
                    - Index object with country names.
                    - Count of visits per country.
        """

        entries = self.df[
            self.df["subject_doc_id"] == doc_id
        ]  # Filter DataFrame by document ID
        countries = entries["visitor_country"]  # Extract the country column
        countries_series = countries.value_counts()  # Make a series of country counts

        return (
            countries,
            countries_series.index,
            countries_series.values,
        )

    def get_browser_analysis(self, doc_id=None):
        """
        Analyze browser usage from the user agent strings for a specific document or all documents.

        Args:
            doc_id (str, optional): The ID of the document to filter by. If None, analyze for all documents.

        Returns:
            tuple: A tuple containing two elements:
                    - A dataframe with all user agent entries for the specified document.
                    - Index object with each browser.
                    - Count of occurrences of each browser.
        """

        if doc_id is None:
            entries = self.df[
                "visitor_useragent"
            ]  # Use all user agent entries if doc_id is None
        else:
            entries = self.df[self.df["subject_doc_id"] == doc_id][
                "visitor_useragent"
            ]  # Filter by doc_id

        browsers = entries.apply(
            self.get_browser_names
        )  # Apply method to extract browser names
        browsers_series = browsers.value_counts()  # Make a series of browser counts

        return (
            browsers,
            browsers_series.index,
            browsers_series.values,
        )

    def get_top_readers(self, doc_id=None):
        """
        Get the top readers based on the total read time for a specific document or all documents.

        Args:
            doc_id (str, optional): The ID of the document to filter by. If None, analyze for all documents.

        Returns:
            DataFrame: A DataFrame containing visitor UUIDs and total read times for the top readers.
        """

        entries = self.df[
            self.df["subject_type"] == "doc"
        ]  # Filter entries for documents only

        if doc_id is None:
            entries = entries[
                ["visitor_uuid", "event_readtime"]
            ]  # Use all documents if doc_id is None
        else:
            entries = entries[entries["subject_doc_id"] == doc_id][
                ["visitor_uuid", "event_readtime"]
            ]  # Filter by doc_id

        top_readers = (
            entries.groupby("visitor_uuid")  # Group by visitor_uuid
            .sum()  # Sum the read times for each group
            .sort_values(
                "event_readtime", ascending=False
            )  # Sort the groups by read time in descending order
            .head(10)  # Select the top 10 readers
        ).reset_index()  # Reset index to turn the result into a DataFrame from a Series

        # Return the UUIDs and read times as separate arrays
        return top_readers["visitor_uuid"].values, top_readers["event_readtime"].values

    def get_also_likes(self, doc_id, user_id):
        """
        For a given document, find other documents liked by the visitors of this document.

        Args:
            doc_id (str): The ID of the document to analyze.

        Returns:
            dict: A dictionary with document IDs as keys, and as values the count of unique visitors and list of these visitors.
        """

        visitors = self.get_visitors(
            doc_id, user_id
        )  # Get unique visitors for the given document

        # Filter the DataFrame for documents visited by these visitors, excluding the original doc_id
        docs_visited = self.get_docs_visited(visitors, doc_id)

        # Group by doc_id, count unique visitors and list them as a set
        grouped = docs_visited.groupby("subject_doc_id")["visitor_uuid"].agg(
            count=lambda x: len(np.unique(x)),  # Count unique visitors
            unique_visitors=lambda x: set(x),  # Create a set of unique visitor UUIDs
        )

        # Sort by count in descending order and get top 10
        top_docs = grouped.sort_values(by="count", ascending=False).head(10)
        top_docs["unique_visitors"] = top_docs["unique_visitors"].apply(list)

        return top_docs.to_dict(orient="index")

    def get_visitors(self, doc_id, user_id):
        """
        Get the unique visitor UUIDs for a given document.

        Args:
            doc_id (str): The ID of the document to analyze.

        Returns:
            Series: A Series containing unique visitor UUIDs for the specified document.
        """

        return self.df[
            (self.df["subject_doc_id"] == doc_id) & (self.df["visitor_uuid"] != user_id)
        ][
            "visitor_uuid"
        ].unique()  # Return unique visitor UUIDs

    def get_docs_visited(self, visitors, doc_id_exclude):
        """
        Get documents visited by a list of visitors, excluding a specific document.

        Args:
            visitors (list): A list of visitor UUIDs.
            doc_id_exclude (str): The ID of the document to exclude from the result.

        Returns:
            DataFrame: A DataFrame of documents visited by the visitors excluding the specified document.
        """

        return self.df[
            self.df["visitor_uuid"].isin(visitors)
            & (self.df["subject_doc_id"] != doc_id_exclude)
        ]  # Return DataFrame of documents visited, excluding the specified document

    def get_browser_names(self, browser):
        """
        Extract the browser name from a user agent string.

        Args:
            browser (str): A user agent string.

        Returns:
            str: The name of the browser identified from the user agent string, with specific checks for mobile browsers.
        """

        user_agent = parse(browser)  # Parse the user agent string

        # Check for specific browser families and return a clean name
        if "Chrome Mobile" in user_agent.browser.family:
            return "Chrome Mobile"

        elif "Mobile Safari" in user_agent.browser.family:
            return "Mobile Safari"

        elif user_agent.is_mobile:
            return "Other Mobile"

        elif (
            ("Chrome" not in user_agent.browser.family)
            and ("Firefox" not in user_agent.browser.family)
            and ("Safari" not in user_agent.browser.family)
            and ("Opera" not in user_agent.browser.family)
            and ("IE" not in user_agent.browser.family)
        ):
            return "Other"
        elif "Chrome" in user_agent.browser.family:
            return "Chrome"
        elif "Firefox" in user_agent.browser.family:
            return "Firefox"
        else:
            return user_agent.browser.family
