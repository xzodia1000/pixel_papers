from pixel_papers.backend.data_reader import DataReader


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


def test_get_top_readers_100k():
    dr = DataReader()
    dr.read_data("./datasets/sample_100k_lines.json")
    top_readers, read_time = dr.get_top_readers()
    print(f"Readers: {top_readers}")
    print(f"Read Time: {read_time}")

    assert top_readers.shape[0] == 10
    assert read_time.shape[0] == 10


def test_get_top_readers_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    top_readers, read_time = dr.get_top_readers()
    print(f"Readers: {top_readers}")
    print(f"Read Time: {read_time}")

    assert top_readers.shape[0] == 10
    assert read_time.shape[0] == 10
