from pixel_papers.backend.data_reader import DataReader


def test_read_data():
    dr = DataReader()
    dr.read_data()
    df = dr.get_df()

    assert df.shape == (10240, 28)


def test_read_data_large():
    dr = DataReader()

    dr.read_data("./datasets/sample_100k_lines.json")
    df = dr.get_df()

    assert df.shape == (102401, 31)

    dr.read_data("./datasets/sample_400k_lines.json")
    df = dr.get_df()
    assert df.shape == (400000, 33)

    dr.read_data("./datasets/sample_600k_lines.json")
    df = dr.get_df()
    assert df.shape == (600000, 31)

    # dr.read_data("./datasets/sample_3m_lines.json")
    # df = dr.get_df()
    # assert df.shape == (3000000, 34)


def test_get_countries():
    dr = DataReader()
    dr.read_data()
    labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 4
    assert count.shape[0] == 4


def test_get_countries_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    labels, count = dr.get_countries("100713205147-2ee05a98f1794324952eea5ca678c026")
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 30
    assert count.shape[0] == 30


def test_get_browser_analysis():
    dr = DataReader()
    dr.read_data()
    labels, count = dr.get_browser_analysis()
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    # with open("./test_outputs/browser_analysis_labels.txt", "w") as f:
    #     for label in labels:
    #         f.write(label + "\n")

    assert labels.shape[0] == 9
    assert count.shape[0] == 9


def test_get_browser_analysis_docid():
    dr = DataReader()
    dr.read_data()
    labels, count = dr.get_browser_analysis(
        "100713205147-2ee05a98f1794324952eea5ca678c026"
    )
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 2
    assert count.shape[0] == 2


def test_get_browser_analysis_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    labels, count = dr.get_browser_analysis()
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    with open("./test_outputs/browser_analysis_labels_600k.txt", "w") as f:
        for label in labels:
            f.write(label + "\n")

    assert labels.shape[0] == 9
    assert count.shape[0] == 9


def test_get_top_readers():
    dr = DataReader()
    dr.read_data()
    top_readers, read_time = dr.get_top_readers()
    print(f"Readers: {top_readers}")
    print(f"Read Time: {read_time}")

    assert top_readers.shape[0] == 10
    assert read_time.shape[0] == 10


def test_get_top_readers_docid():
    dr = DataReader()
    dr.read_data()
    top_readers, read_time = dr.get_top_readers(
        "100713205147-2ee05a98f1794324952eea5ca678c026"
    )
    print(f"Readers: {top_readers}")
    print(f"Read Time: {read_time}")

    assert top_readers.shape[0] == 4
    assert read_time.shape[0] == 4


def test_get_top_readers_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    top_readers, read_time = dr.get_top_readers()
    print(f"Readers: {top_readers}")
    print(f"Read Time: {read_time}")

    assert top_readers.shape[0] == 10
    assert read_time.shape[0] == 10
