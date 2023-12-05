from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils


def test_countries_bar_chart():
    dr = DataReader()
    dr.read_data()
    _, labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    gu = GraphUtils()
    plot = gu.plot_bar_chart(
        labels, count, "Countries Distribution", "Countries", "Count"
    )
    plot.show()

    assert True


def test_countries_bar_chart_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    _, labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    gu = GraphUtils()
    plot = gu.plot_bar_chart(
        labels, count, "Countries Distribution", "Countries", "Count"
    )
    plot.show()

    assert True


def test_browser_bar_chart():
    dr = DataReader()
    dr.read_data()
    _, labels, count = dr.get_browser_analysis()
    gu = GraphUtils()
    plot = gu.plot_bar_chart(labels, count, "Browser Distribution", "Browser", "Count")
    plot.show()

    assert True


def test_browser_bar_chart_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    _, labels, count = dr.get_browser_analysis()
    gu = GraphUtils()
    plot = gu.plot_bar_chart(labels, count, "Browser Distribution", "Browser", "Count")
    plot.show()

    assert True
