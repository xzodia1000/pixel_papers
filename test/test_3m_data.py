from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils


def test_read_data():
    dr = DataReader()
    dr.read_data("./datasets/sample_3m_lines.json")
    df = dr.get_df()

    assert df.shape[0] == 3000000


def test_histogram():
    dr = DataReader()
    dr.read_data("./datasets/sample_3m_lines.json")
    data, _, _ = dr.get_browser_analysis()
    gu = GraphUtils()
    plot = gu.plot_histogram(data, "Browser Distribution", "Browser", "Count")
    plot.show()

    assert True
