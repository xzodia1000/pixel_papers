from pixel_papers.backend.data_reader import DataReader
from pixel_papers.backend.graph_utils import GraphUtils


def test_also_likes_graph():
    dr = DataReader()
    dr.read_data()
    docs = dr.get_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026", "489c02f3e258c199"
    )

    gu = GraphUtils()

    dot = gu.plot_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026",
        docs,
        "Also Likes Graph",
        "489c02f3e258c199",
    )
    # dot.render("./test_outputs/also_likes_graph.gv", view=True)
    dot.render("./test_outputs/also_likes_graph", view=False, format="dot")
    dot.render("./test_outputs/also_likes_graph", view=True, format="pdf")

    assert True


def test_also_likes_graph_100k():
    dr = DataReader()
    dr.read_data("./datasets/sample_100k_lines.json")
    docs = dr.get_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026", "489c02f3e258c199"
    )

    gu = GraphUtils()

    dot = gu.plot_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026",
        docs,
        "Also Likes Graph",
        "489c02f3e258c199",
    )

    dot.render("./test_outputs/also_likes_graph_100k", view=False, format="dot")
    dot.render("./test_outputs/also_likes_graph_100k", view=True, format="pdf")

    assert True


def test_also_likes_graph_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    docs = dr.get_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026", "489c02f3e258c199"
    )

    gu = GraphUtils()

    dot = gu.plot_also_likes(
        "100713205147-2ee05a98f1794324952eea5ca678c026",
        docs,
        "Also Likes Graph",
        "489c02f3e258c199",
    )

    dot.render("./test_outputs/also_likes_graph_600k", view=False, format="dot")
    dot.render("./test_outputs/also_likes_graph_600k", view=True, format="pdf")

    assert True
