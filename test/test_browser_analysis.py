from pixel_papers.backend.data_reader import DataReader


def test_get_browser_analysis():
    dr = DataReader()
    dr.read_data()
    _, labels, count = dr.get_browser_analysis()
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
    _, labels, count = dr.get_browser_analysis(
        "100713205147-2ee05a98f1794324952eea5ca678c026"
    )
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 2
    assert count.shape[0] == 2


def test_get_browser_analysis_600k():
    dr = DataReader()
    dr.read_data("./datasets/sample_600k_lines.json")
    _, labels, count = dr.get_browser_analysis()
    print(f"Labels: {labels.tolist()}")
    print(f"Count: {count.tolist()}")

    assert labels.shape[0] == 9
    assert count.shape[0] == 9
