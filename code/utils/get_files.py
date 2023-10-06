import gdown


def get_data_from_google_drive(
    file_id: str, file_path: str = "/data/dataset/student_data.csv"
):
    """download the csv file from google drive

    Args:
        file_id (str): get it from the shareable link in google drive
        file_path (str, optional): path to the donwloaded file. Defaults to "/data/dataset/student_data.csv".
    """
    # Download the file
    gdown.download(
        url=f"https://drive.google.com/uc?id={file_id}",
        output=file_path,
        quiet=False,
    )
