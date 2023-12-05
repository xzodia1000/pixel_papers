from pixel_papers.backend.data_reader import DataReader


def test_read_data():
    dr = DataReader()
    dr.read_data()
    df = dr.get_df()

    assert df.shape == (10240, 28)


def test_read_data_100k():
    dr = DataReader()

    dr.read_data("./datasets/sample_100k_lines.json")
    df = dr.get_df()

    assert df.shape == (102401, 31)


def test_read_data_400k():
    dr = DataReader()

    dr.read_data("./datasets/sample_400k_lines.json")
    df = dr.get_df()

    assert df.shape == (400000, 33)


def test_read_data_600k():
    dr = DataReader()

    dr.read_data("./datasets/sample_600k_lines.json")
    df = dr.get_df()

    assert df.shape == (600000, 31)


# def test_read_data_3m():
#     dr = DataReader()

#     dr.read_data("./datasets/sample_3m_lines.json")
#     df = dr.get_df()

#     assert df.shape == (3000000, 34)
