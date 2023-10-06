import gdown


def get_data_from_google_drive(
    url: str, file_path: str = "/data/dataset/student_data.csv"
):
    """_summary_

    Args:
        url (_type_): _description_
        file_path (str, optional): _description_. Defaults to '/data/dataset/student_data.csv'.
    """
    # Download the file
    gdown.download(url, file_path, quiet=False)
