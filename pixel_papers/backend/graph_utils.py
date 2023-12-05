from matplotlib import pyplot as plt
from graphviz import Digraph
import matplotlib.cm as cm
import numpy as np


class GraphUtils:
    def plot_bar_chart(self, x, y, title, x_label, y_label):
        """
        Plot a bar chart using the provided data.

        Args:
            x: A sequence of x-axis labels (categories).
            y: A sequence of y-values for each x-label.
            title: The title of the graph.
            x_label: The label for the x-axis.
            y_label: The label for the y-axis.
        """
        # Get a color map and generate a unique color for each bar
        color_map = cm.get_cmap("plasma", len(x))
        colors = color_map(range(len(x)))

        # Set up the plot
        plt.figure(figsize=(10, 8))
        plt.bar(x, y, color=colors)
        plt.title(title)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()

        return plt

    def plot_histogram(self, x, title, x_label, y_label):
        """
        Plot a histogram using the provided data.

        Args:
            x: A sequence of values to be binned.
            title: The title of the graph.
            x_label: The label for the x-axis.
            y_label: The label for the y-axis.
        """
        # Determine the number of bins for the histogram
        bins = len(np.unique(x))
        # Get a color map and generate a unique color for each bin
        color_map = cm.get_cmap("plasma", bins)
        colors = color_map(range(bins))

        # Set up the plot
        plt.figure(figsize=(10, 8))
        _, _, patches = plt.hist(x, bins=bins, edgecolor="black")

        # Color each bin with the corresponding color
        for patch, color in zip(patches, colors):
            patch.set_facecolor(color)

        plt.title(title)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()

        return plt

    def plot_also_likes(self, input_doc, data, title, user="New User"):
        """
        Plot a directed graph showing the documents also liked by users who read a particular document.

        Args:
            input_doc: The ID of the initial document.
            data: A dictionary where each key is a document ID, and the value is a dictionary with counts and unique visitors.
            title: The title of the graph.
            user: The user ID of the new reader (default is "New User").
        """
        dot = Digraph(comment=title)

        # Graph settings
        dot.attr("graph", rankdir="TB", size="8,5")
        dot.attr("node", fontsize="10", height="0.5")
        dot.attr("edge", arrowsize="0.5")

        # Add nodes for the input document and the new user
        dot.node(
            self.truncate(input_doc),
            self.truncate(input_doc),
            color="green",
            style="filled",
            shape="circle",
        )
        dot.node(
            self.truncate(user),
            self.truncate(user),
            color="green",
            style="filled",
            shape="box",
        )

        # Connect the new user to the input document
        dot.edge(self.truncate(user), self.truncate(input_doc))

        # Add nodes and edges for the related documents and their visitors
        for doc_id, info in data.items():
            dot.node(
                self.truncate(doc_id),
                self.truncate(doc_id),
                shape="circle",
            )

            for visitor in info["unique_visitors"]:
                dot.node(self.truncate(visitor), self.truncate(visitor), shape="box")
                dot.edge(self.truncate(visitor), self.truncate(doc_id))
                dot.edge(self.truncate(visitor), self.truncate(input_doc))

        # Render and view the graph
        return dot

    def truncate(self, s):
        """
        Truncate the string to show only the last four characters, typically used to shorten IDs.

        Args:
            s: The string to truncate.

        Returns:
            The truncated string.
        """
        return s[-4:]
