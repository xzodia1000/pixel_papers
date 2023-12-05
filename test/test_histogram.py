from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils


def test_countries_histogram():
    dr = DataReader()
    dr.read_data()
    data, _, _ = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    gu = GraphUtils()
    plot = gu.plot_histogram(data, "Countries Distribution", "Countries", "Count")
    plot.show()

    assert True


def test_countries_histogram_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    data, _, _ = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    gu = GraphUtils()
    plot = gu.plot_histogram(data, "Countries Distribution", "Countries", "Count")
    plot.show()

    assert True


def test_browser_histogram():
    dr = DataReader()
    dr.read_data()
    data, _, _ = dr.get_browser_analysis()
    gu = GraphUtils()
    plot = gu.plot_histogram(data, "Browser Distribution", "Browser", "Count")
    plot.show()

    assert True


def test_browser_histogram_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    data, _, _ = dr.get_browser_analysis()
    gu = GraphUtils()
    plot = gu.plot_histogram(data, "Browser Distribution", "Browser", "Count")
    plot.show()

    assert True
