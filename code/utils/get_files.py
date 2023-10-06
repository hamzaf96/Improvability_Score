import gdown


def get_data_from_google_drive(
    file_id: str, file_path: str = "/data/dataset/student_data.csv"
):
    """download the csv file from google drive

    Args:
        file_id (str): _description_
        file_path (str, optional): _description_. Defaults to "/data/dataset/student_data.csv".
    """
    # Download the file
    gdown.download(
        url=f"https://drive.google.com/uc?id={file_id}",
        output=file_path,
        quiet=False,
    )
