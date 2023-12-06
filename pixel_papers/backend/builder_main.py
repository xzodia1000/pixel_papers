import pandas as pd
from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils
from pycountry_convert import country_alpha2_to_continent_code


class BuilderMain:
    def __init__(self):
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
        self.dr.read_data(path)

    def views_by_country(self, doc_id):
        countries, labels, count = self.dr.get_countries(doc_id)
        plot_bar = self.gu.plot_bar_chart(
            labels, count, "Countries Distribution", "Country", "Count"
        )
        plot_hist = self.gu.plot_histogram(
            countries, "Countries Distribution", "Country", "Count"
        )

        return plot_bar, plot_hist

    def views_by_continent(self, doc_id):
        countries, labels, count = self.dr.get_countries(doc_id)
        df_continents = pd.DataFrame({"Country": labels, "Count": count})
        df_continents["Continent"] = df_continents["Country"].apply(self.get_continent)
        continent_count = df_continents.groupby("Continent")["Count"].sum()

        continents = countries.map(self.get_continent)

        plot_bar = self.gu.plot_bar_chart(
            continent_count.index,
            continent_count.values,
            "Continents Distribution",
            "Continent",
            "Count",
        )

        plot_hist = self.gu.plot_histogram(
            continents, "Continents Distribution", "Continent", "Count"
        )

        return plot_bar, plot_hist

    def views_by_browser(self, doc_id=None):
        browser, labels, count = self.dr.get_browser_analysis(doc_id)
        plot_bar = self.gu.plot_bar_chart(
            labels, count, "Browser Distribution", "Browser", "Count"
        )
        plot_hist = self.gu.plot_histogram(
            browser, "Browser Distribution", "Browser", "Count"
        )

        return plot_bar, plot_hist

    def reader_profiles(self, doc_id=None):
        top_readers, read_time = self.dr.get_top_readers(doc_id)
        return top_readers, read_time

    def also_likes(self, doc_id, user_id):
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
            view=True,
            format="pdf",
        )

        return docs_list, dot

    def get_continent(self, countrye_code):
        try:
            return self.continent_names[country_alpha2_to_continent_code(countrye_code)]
        except KeyError:
            return "Other"

    def truncate(self, s):
        """
        Truncate the string to show only the last four characters, typically used to shorten IDs.

        Args:
            s: The string to truncate.

        Returns:
            The truncated string.
        """
        return s[-4:]
