from pixel_papers.backend.builder_main import BuilderMain


def test_views_by_continents():
    builder = BuilderMain()
    builder.read_file()
    plot = builder.views_by_continent("100713205147-2ee05a98f1794324952eea5ca678c026")
    plot.show()

    assert True


def test_views_by_continents_600k():
    builder = BuilderMain()
    builder.read_file("./datasets/sample_600k_lines.json")
    plot = builder.views_by_continent("100713205147-2ee05a98f1794324952eea5ca678c026")
    plot.show()

    assert True
