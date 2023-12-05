from pixel_papers.backend.data_reader import DataReader


def test_get_countries():
    dr = DataReader()
    dr.read_data()
    _, labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 4
    assert count.shape[0] == 4


def test_get_countries_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    _, labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 30
    assert count.shape[0] == 30
