import argparse
import os
from pixel_papers.backend.builder_main import BuilderMain


def milliseconds_to_minutes(milliseconds):
    """Convert milliseconds to minutes."""
    return milliseconds / (1000 * 60)


def validate_task_id(task_id):
    """Validate the task ID."""
    valid_ids = ["1", "2a", "2b", "3a", "3b", "4", "5", "6"]
    if task_id not in valid_ids:
        print("Invalid task ID.")
        exit(1)


def process_file(bm, file_name):
    """Process the file based on the provided file name."""
    if file_name is None:
        print(
            "File path not provided. Using default file. (datasets/sample_small.json)"
        )
        bm.read_file()
    else:
        if os.path.exists(file_name):
            bm.read_file(file_name)
        else:
            print("File does not exist.")
            exit(1)


def execute_task(bm, task_id, user_uuid, doc_uuid):
    """Execute the specified task."""
    if "2" in task_id and doc_uuid is None:
        print("Document UUID not provided for views by country/continent.")
        exit(1)

    print("Loading...")
    if task_id in ["2a", "2b", "3a", "3b"]:
        if task_id == "2a":
            plot_hist = bm.views_by_country(doc_uuid)
        elif task_id == "2b":
            plot_hist = bm.views_by_continent(doc_uuid)
        else:
            plot_hist = bm.views_by_browser()

        plot_hist.show()
    elif task_id == "4":
        top_readers, time = bm.reader_profiles()
        for i, reader in enumerate(top_readers):
            print(
                f"Reader {i+1}: {reader} - {milliseconds_to_minutes(time[i])} minutes"
            )
    elif task_id in ["5", "6"]:
        if user_uuid is None or doc_uuid is None:
            print("User UUID or Document UUID not provided for 'also likes'.")
            exit(1)
        docs, _ = bm.also_likes(doc_uuid, user_uuid)
        for i, doc in enumerate(docs):
            print(f"Document {i+1}: {doc}")
        print(f"Graph saved to ./program_outputs/also_likes_graph_{doc_uuid[-4:]}.pdf")


def main(task_id, file_name=None, user_uuid=None, doc_uuid=None):
    """Main function to run the tasks."""
    validate_task_id(task_id)

    if task_id == "1":
        print("Python 3 was used to develop this program.")
        exit(0)

    bm = BuilderMain()
    process_file(bm, file_name)
    execute_task(bm, task_id, user_uuid, doc_uuid)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pixel Papers - Data Analysis Tool")
    parser.add_argument("-u", "--user_uuid", help="User UUID", required=False)
    parser.add_argument("-d", "--doc_uuid", help="Document UUID", required=False)
    parser.add_argument("-t", "--task_id", help="Task ID", required=True)
    parser.add_argument("-f", "--file_path", help="File Path", required=False)

    args = parser.parse_args()
    main(args.task_id, args.file_path, args.user_uuid, args.doc_uuid)
