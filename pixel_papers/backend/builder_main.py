import pandas as pd
from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils
from pycountry_convert import country_alpha2_to_continent_code


class BuilderMain:
    def __init__(self):
        """
        Constructor for BuilderMain class. Initializes the DataReader and GraphUtils objects,
        and sets up a dictionary for continent names.
        """
        self.dr = DataReader()
        self.gu = GraphUtils()

        self.continent_names = {
            "AF": "Africa",
            "AS": "Asia",
            "EU": "Europe",
            "NA": "North America",
            "OC": "Oceania",
            "SA": "South America",
            "AN": "Antarctica",
        }

    def read_file(self, path="./datasets/sample_small.json"):
        """
        Reads data from a specified file.

        Args:
            path (str): The file path to read from. Defaults to "./datasets/sample_small.json".
        """
        self.dr.read_data(path)

    def views_by_country(self, doc_id, hist=True):
        """
        Generates bar chart and histogram for views by country based on a document ID.

        Args:
            doc_id (str): The document ID to analyze.

        Returns:
            tuple: A tuple containing the bar chart and histogram plot objects.
        """
        countries, labels, count = self.dr.get_countries(doc_id)

        if hist:
            plot = self.gu.plot_histogram(
                countries, "Histogram - Countries Distribution", "Country", "Count"
            )
        else:
            plot = self.gu.plot_bar_chart(
                labels, count, "Bar Chart - Countries Distribution", "Country", "Count"
            )

        return plot

    def views_by_continent(self, doc_id, hist=True):
        """
        Generates bar chart and histogram for views by continent based on a document ID.

        Args:
            doc_id (str): The document ID to analyze.

        Returns:
            tuple: A tuple containing the bar chart and histogram plot objects.
        """
        countries, labels, count = self.dr.get_countries(doc_id)
        df_continents = pd.DataFrame({"Country": labels, "Count": count})
        df_continents["Continent"] = df_continents["Country"].apply(self.get_continent)
        continent_count = df_continents.groupby("Continent")["Count"].sum()

        continents = countries.map(self.get_continent)

        if hist:
            plot = self.gu.plot_histogram(
                continents, "Histogram - Continents Distribution", "Continent", "Count"
            )
        else:
            plot = self.gu.plot_bar_chart(
                continent_count.index,
                continent_count.values,
                "Bar Chart - Continents Distribution",
                "Continent",
                "Count",
            )

        return plot

    def views_by_browser(self, doc_id=None, hist=True):
        """
        Generates bar chart and histogram for views by browser.

        Args:
            doc_id (str, optional): The document ID to analyze. Defaults to None.

        Returns:
            tuple: A tuple containing the bar chart and histogram plot objects.
        """
        browser, labels, count = self.dr.get_browser_analysis(doc_id)

        if hist:
            plot = self.gu.plot_histogram(
                browser, "Histogram - Browser Distribution", "Browser", "Count"
            )
        else:
            plot = self.gu.plot_bar_chart(
                labels, count, "Bar Chart - Browser Distribution", "Browser", "Count"
            )

        return plot

    def reader_profiles(self, doc_id=None):
        """
        Retrieves top reader profiles.

        Args:
            doc_id (str, optional): The document ID to analyze. Defaults to None.

        Returns:
            tuple: A tuple of top readers and their read times.
        """
        top_readers, read_time = self.dr.get_top_readers(doc_id)
        return top_readers, read_time

    def also_likes(self, doc_id, user_id, render=True):
        """
        Analyzes and plots the "also likes" graph for a given document and user.

        Args:
            doc_id (str): The document ID.
            user_id (str): The user ID.

        Returns:
            tuple: A tuple containing the list of documents and the graph object.
        """
        docs_dict = self.dr.get_also_likes(doc_id, user_id)
        docs_list = docs_dict.keys()
        dot = self.gu.plot_also_likes(doc_id, docs_dict, "Also Likes Graph", user_id)

        dot.render(
            f"./program_outputs/also_likes_graph_{self.truncate(doc_id)}",
            view=False,
            format="dot",
        )

        dot.render(
            f"./program_outputs/also_likes_graph_{self.truncate(doc_id)}",
            view=render,
            format="pdf",
        )

        return docs_list, dot

    def get_continent(self, country_code):
        """
        Converts a country code to its corresponding continent name.

        Args:
            country_code (str): The alpha-2 country code.

        Returns:
            str: The name of the continent or 'Other' if the country code is not found.
        """
        try:
            return self.continent_names[country_alpha2_to_continent_code(country_code)]
        except KeyError:
            return "Other"

    def truncate(self, s):
        """
        Truncate the string to show only the last four characters, typically used to shorten IDs.

        Args:
            s (str): The string to truncate.

        Returns:
            str: The truncated string.
        """
        return s[-4:]
