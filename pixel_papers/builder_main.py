from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils


class BuilderMain:
    def __init__(self):
        self.dr = DataReader()
        self.gu = GraphUtils()

    def read_file(self, path="./datasets/sample_small.json"):
        self.dr.read_data(path)
    