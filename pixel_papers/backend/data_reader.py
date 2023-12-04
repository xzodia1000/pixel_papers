import pandas as pd


class DataReader:
    def __init__(self):
        self.df = None
        self.browser_pattern = r"Chrome|Firefox|Safari|Opera||MSIE|Mozilla"

    def read_data(self, path="./datasets/sample_small.json"):
        self.df = pd.read_json(path, lines=True)

    def get_df(self):
        return self.df

    def get_countries(self, doc_id):
        entries = self.df[self.df["subject_doc_id"] == doc_id]
        countries = entries["visitor_country"]
        countries_series = countries.value_counts()
        return countries_series.index, countries_series.values

    def get_browser_analysis(self, doc_id=None):
        if doc_id is None:
            entries = self.df["visitor_useragent"]
        else:
            entries = self.df[self.df["subject_doc_id"] == doc_id]["visitor_useragent"]

        browsers = entries.apply(self.get_browser_names).value_counts()
        return browsers.index, browsers.values

    def get_top_readers(self, doc_id=None):
        entries = self.df[self.df["subject_type"] == "doc"]
        if doc_id is None:
            entries = entries[["visitor_uuid", "event_readtime"]]
        else:
            entries = entries[entries["subject_doc_id"] == doc_id][
                ["visitor_uuid", "event_readtime"]
            ]

        top_readers = (
            entries.groupby("visitor_uuid")
            .sum()
            .sort_values("event_readtime", ascending=False)
            .head(10)
        ).reset_index()

        return top_readers["visitor_uuid"].values, top_readers["event_readtime"].values

    def get_browser_names(self, browser):
        if "Chrome" in browser:
            return "Chrome"
        elif "Firefox" in browser:
            return "Firefox"
        elif "Safari" in browser and "Chrome" not in browser:
            return "Safari"
        elif (
            "MSIE" in browser or "Trident" in browser or "Internet Explorer" in browser
        ):
            return "Internet Explorer"
        elif "Opera" in browser or "OPR" in browser:
            return "Opera"
        elif "UCBrowser" in browser:
            return "UCBrowser"
        elif ("iPhone" in browser or "iPad" in browser) and "Chrome" not in browser:
            return "Safari (iOS)"
        elif "OviBrowser" in browser:
            return "OviBrowser"
        return "Other"
