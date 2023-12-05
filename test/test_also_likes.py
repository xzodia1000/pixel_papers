from pixel_papers.backend.data_reader import DataReader


def test_get_also_likes():
    dr = DataReader()
    dr.read_data()
    docs = dr.get_also_likes("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(docs)

    assert len(docs) == 10


def test_get_also_likes_100k():
    dr = DataReader()
    dr.read_data("./datasets/sample_100k_lines.json")
    docs = dr.get_also_likes("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(docs)

    assert len(docs) == 10


def test_get_also_likes_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    docs = dr.get_also_likes("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(docs)

    assert len(docs) == 10
